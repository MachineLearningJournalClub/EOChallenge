
#%%
import math
import numpy as np
import pandas as pd

from kneed import KneeLocator

from sklearn.cluster import DBSCAN, AgglomerativeClustering
from sklearn.neighbors import NearestNeighbors
from sklearn.decomposition import PCA


import multiprocessing

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import keras
from keras import Sequential
from keras.layers import Dense, RepeatVector, TimeDistributed
from keras.layers import LSTM

import keras
from tensorflow.keras import Sequential
from keras.layers import *
from keras.callbacks import *

import tensorflow as tf
from sklearn.model_selection import train_test_split

import sklearn

import pandas as pd

#%%

def get_cpu_number():
    return multiprocessing.cpu_count()


def dimensionality_reduction(vectors, n_reduction=2):
    print('Number of dimensions is {}'.format(n_reduction))
    pca = PCA(n_components=n_reduction, svd_solver='full')
    pca.fit(vectors)
    return pca.transform(vectors)

def kneighbors(vectors):
    """
    Calculates average distances for k-nearest neighbors
    :return:
    """
    k = round(math.sqrt(len(vectors)))
    print('K-neighbours = {}'.format(k))
    nbrs = NearestNeighbors(n_neighbors=k, n_jobs=-1, algorithm='auto').fit(vectors) #-1 means using all processors       
    distances, indices = nbrs.kneighbors(vectors)
    distances = [np.mean(d) for d in np.sort(distances, axis=0)]
    return distances
    
def epsilon_search(vectors):
    """
    Search epsilon for the DBSCAN clusterization
    :return:
    """
    distances=kneighbors(vectors)
    kneedle = KneeLocator(distances, list(range(len(distances))), online=True)
    epsilon = np.mean(list(kneedle.all_elbows))
    if epsilon == 0.0:
        epsilon = np.mean(distances)
    return epsilon

def dbscan(df,min_samples=5,pca=True):
    """
    Execution of the DBSCAN clusterization algorithm.
    Returns cluster labels
    :return:
    """
    cpu_number=get_cpu_number()
    vectors=df['Vector'].values.tolist()
    if pca:
        vectors = dimensionality_reduction(vectors)
    distances=kneighbors(vectors)
    epsilon=epsilon_search(vectors)
    cluster_labels = DBSCAN(eps=epsilon,
    min_samples=min_samples,
     n_jobs=cpu_number) \
    .fit_predict(vectors)
    df['cluster'] = cluster_labels
    print('DBSCAN finished with {} clusters'.format(len(set(cluster_labels))))
    return pd.DataFrame.from_dict([item for item in df.groupby('cluster').apply(func=gb_regroup)], orient='columns').sort_values(by=['cluster_size'], ascending=False)
    #return df

def gb_regroup(gb):
    #indices = [i for sublist in gb['cluster'].values for i in sublist]
    states=[sublist for sublist in gb['State'].values]
    size = len(states)    
    return {'cluster_size': size,'state':states}


###############################################################
###############################################################


#%%
def create_fake_data(len = 143, n = 100, test_size = 0.2):
    # Creates dataset similar to the ones we have
    data = []

    for i in range(n):
        data.append(np.cumsum(np.random.rand(len)*2 - 1)) 

    x_train, y_train, x_test, y_test = train_test_split(data, data, test_size = test_size, random_state = 42)

    return x_train, y_train, x_test, y_test

def preprocessing(test_size = 0.25, path = '', len = 0, safe_len = 144):
    # Loads data and fills nan
    
    data_dict = pd.read_pickle(path)

    for entry in data_dict:
        data_dict[entry].drop(data_dict[entry].head(-len).index, inplace = True)
        data_dict[entry].interpolate(inplace = True)
        data_dict[entry].fillna(method = 'backfill')
    
    columns = []

    for entry in data_dict:
        for col in data_dict[entry]:
            if col != 'time':
                columns.append(np.array(data_dict[entry][col]))

    columns = [i/i.max() for i in columns if i.shape[0] == safe_len ]
                
    x_train, x_test, y_train, y_test = train_test_split(columns, columns, test_size = test_size, random_state = 42)

    return x_train, x_test, y_train, y_test

def train_autoencoder(x_train, embedding_dimension = 2):
    inp_len = len(x_train[0])

    model = Sequential([Dense(inp_len, activation = 'relu'),
    Dense(100, activation = 'relu'),
    Dense(50, activation = 'relu'),
    Dense(25, activation = 'relu'),
    Dense(embedding_dimension, activation = 'relu', name = 'encoder'),
    Dense(25, activation = 'relu'),
    Dense(50, activation = 'relu'),
    Dense(100, activation = 'relu'),
    Dense(inp_len)])

    opt = tf.keras.optimizers.Adam(
        learning_rate=0.0005,
        beta_1=0.9,
        beta_2=0.999,
        epsilon=1e-07,
        amsgrad=False,
        name="Adam")

    model.compile(optimizer=opt,
                loss='mean_squared_error',
                metrics=['mae','acc'])

    earlyStopping = EarlyStopping(monitor='val_loss', patience=25, verbose=0, mode='min')
    mcp_save = ModelCheckpoint('.mdl_wts.hdf5', save_best_only=True, monitor='val_loss', mode='min')
    reduce_lr_loss = ReduceLROnPlateau(monitor='val_loss', factor=0.1, patience=7, verbose=1, epsilon=1e-4, mode='min')

    history = model.fit(x_train, x_train, epochs = 10000, batch_size = 16, verbose = 1) #callbacks=[earlyStopping],

    return model, history

def evaluate_autoencoder(model, x_test, index = 0):
    # Make predictions on entire test set
    predictions = model.predict(x_test)

    # Use score method to get accuracy of model
    mse = sklearn.metrics.mean_squared_error(x_test, predictions)

    print(mse)

    plt.figure(figsize = (20,20))
    plt.plot(x_train[index], color = 'red')
    plt.plot(predictions[index], color = 'green')
    #plt.plot(x_train[0] - predictions[0], color = 'grey')

def get_embedding(model, data):
    intermediate_layer_model = keras.Model(inputs=model.input,
                                 outputs=model.get_layer('encoder').output)

    embedding = intermediate_layer_model.predict(data)

    return embedding

def embed_dataset(path, model,len = 0, safe_len = 144, embedding_dimension = 5):
    data_dict = pd.read_pickle(path)

    for entry in data_dict:
        data_dict[entry].drop(data_dict[entry].head(-len).index, inplace = True)
        data_dict[entry].interpolate(inplace = True)
        data_dict[entry].fillna(method = 'backfill')
    
    columns = []

    for entry in data_dict:
        for col in data_dict[entry]:
            if col != 'time':
                columns.append(np.array(data_dict[entry][col]))

    columns = [i/i.max() for i in columns if i.shape[0] == safe_len]

    embedding = get_embedding(model, np.array(columns))

    emb_dict = {}

    for entry, emb in zip(data_dict, embedding):
        emb_dict[entry] = emb

    return emb_dict

def pipeline(embedding_dimension):
    x_train, x_test, y_train, y_test = preprocessing(path = '2018_2020_O3_NO2_SO2_CO_CH4_all.pkl', test_size=0.01)

    model, history = train_autoencoder(np.array(x_train), embedding_dimension=5)

    #evaluate_autoencoder(model, np.array(x_test), index = np.random.randint(0,len(x_test)-1))
    evaluate_autoencoder(model, np.array(x_train), index = np.random.randint(0,len(x_train)-1))

    emb = get_embedding(model, np.array(x_train))

    embedding = embed_dataset('2018_2020_O3_NO2_SO2_CO_CH4_all.pkl', model)

    df = pd.DataFrame()
    df['State'] = embedding.keys()
    df['Vector'] = [embedding[val] for val in embedding.keys()]

    cl=dbscan(df,pca=True)   

    pca = dimensionality_reduction([embedding[val] for val in embedding.keys()])

    df['PCA'] = [i for i in pca]

    for i in df['cluster'].unique():
        dat = df.query('cluster == ' + str(i))['PCA']
        plt.scatter([i[0] for i in dat], [i[1] for i in dat])
    plt.title(embedding_dimension)
    plt.show()
    plt.close()


for i in range(2,10):
    pipeline(i)
#%%

# %%

# %%

