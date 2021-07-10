# The Challenge

The COVID-19 pandemic has had different impacts in different regions of the world. The EO Dashboard Hackathon [https://www.eodashboardhackathon.org/](url) supported by NASA (National Aeronautics and Space Administration), ESA (European Space Agency) and JAXA (Japan Aerospace Exploration Agency), allowed people from all over the world to tackle the problem of analysing such differences from several points of view. In taking part in the competition we decided to face the comparative analysis challenge [https://www.eodashboardhackathon.org/challenges/interconnected-earth-system-impact/comparative-analysis/details](url). This repository collects all the files used to perform such analysis and presents some novel approaches aimed to improve the current EODashboard.

# Background

2020: under the pandemic wave, the world slowed down. Industries and transports were heavily impacted and beyond the effects on private lives and social interactions, the pandemic had repercussions on the environment. The question leading us was how much of these changes we could actually see in data from satellite. We focused on variations in greenhouse gases (SO2, NO2, O3, CO and CH4) and on the differences of these variations across different world countries. To this end we performed a time-oriented analysis on time series and a complementary geography-oriented analysis, based on unsupervised feature extracting, to highlight differences between countries.

# Data analysis

Being part of the Machine Learning Journal Club we approached the problem starting from our knowledge of Data analysis and Machine Learning. For the time-oriented analysis we employ the Prophet algorithm, implemented by the Facebook's Core Data Science team to do forecasting prediction [https://facebook.github.io/prophet/](url).
As a complementary route, the geography-oriented analysis aimed to quantify the differences in behaviours of a group of countries in Europe, Asia and America during the pandemic: to this end we used a method that performs dimensionality reduction on the time serie of the given gases (embedding). This is achieved by using a Neural Network Autoencoder, which is basically a perceptron that tries to create an output which is equal to its input. We trained the NN and we got the output on the intermediate layer of it (in our specific model it is 9-dimensional). Roughly speaking, we "compressed" the whole information from the time series in a single vector, namely the internal reppresentation in the autoencoder. We then combined the different vectors given by every time serie for a given country (one for every gas) by joining them. Eventually DBScan is used to clusterize the results, via PCA.

# Objectives

Our ultimate goal is to create a feasible application to the EODashboard in order to quantify the socio-economic impacts that the pandemic had on different cuntries. We used different varibles from the Copernicus Sentinel 5 as proxies; in particular we employed SO2, NO2, O3, CO and CH4. More variables can of course be added to further improve our work.

# How to Use

All the notebooks used for the analysis in this competition are in the folder 'notebook'. Since the time was tight we cannot exclude some errors might have happened: if you find any, please let us know! Here the list of the most relevant libraries we employed:

- xcube_sh: needed to retrieve data. In order to use this library you have to install xcube. Follow the instruction here: [https://github.com/dcs4cop/xcube-sh](url) (important note: it is necessary to create a sentinel-hub or data-cube account in order to retrieve data);
- numpy, pandas to manage data;
- pickle: used to save the data on files;
- kneed;
- keras, tensorflow: used to build and train the NN.

We used the following pipeline in order to perform our analysis:

- S5PL2.ipynb: retrieve data and save them in the "data/data_countries" folder;
- merge_files.ipynb: take all the previously files and merge them in two files. In the first one all the Nan values are still present, while in the second they have been taken care of. These files are saved in the "data/data_merged" directory;
- csv.ipynb: notebook used to compute the mean over the pre-CoViD period and the pandemic one. It saves these values in the "data/csv" folder. These data will then be plotted in the map.html.

Different kinds of analysis can be performed at this point:

- geography-oriented (autoenconder.ipynb): an autoencoder architecture is used to reduce time series to a bunch of scalar values, representing emission changes during a given period; such values are then used to differentiate between countries. This kind of analysis can be further improved to obtain a more clear clustering.
- time-oriented (prophet_analysis2.ipynb): a country-specific, diachronic time series study to understand the change in emission pattern during the pandemic.

# Map

The map folder contains the useful files in order to visualise the results. The html file is the final result, while the source code is in the python notebook. Data are stored in the 'data' folder. This map is used as a possible exampe for the implementation of the EODashboard.
