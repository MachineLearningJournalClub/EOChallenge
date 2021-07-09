# The Challenge
source: 

The COVID-19 pandemic has had different impacts in different regions of the world. The EO Dashboard Hackathon [https://www.eodashboardhackathon.org/](url) supported by NASA (National Aeronautics and Space Administration), ESA (European Space Agency) and JAXA (Japan Aerospace Exploration Agency) allow  people from all over the world to tackle this problem from many different point of view. In the course of such competition we decice to face the comparative analysis challenge [https://www.eodashboardhackathon.org/challenges/interconnected-earth-system-impact/comparative-analysis/details](url). This repository collect all the files used to perform such analysis and present some novelties approach that can be inserted in the current EODashboard.

# Background
2020: under the pandemic wave, the world slowed down. Industries and transports were heavily impacted and beyond the effects on private lives and social interactions, the pandemic had repercussions on the environment. The question leading us was how much of these changes we could actually see in data from satellite. We focused on variations in greenhouse gases (SO2, NO2, O3, CO and CH4) and ozone, and on the differences of these variations across different world countries. To this end we performed a time-oriented analysis on time series and a complementary geography-oriented analysis, based on unsupervised feature extracting, to highlight differences between countries.

# Data analysis
As a part of the Machine Learning Journal Club we decide to employ our knowledge in the Data analysis and Machine Learning to deal with this task. For the time-oriented analysis we employ the Prophet algorithm that was implemented by the Facebook's Core Data Science team to do forecasting prediction [https://facebook.github.io/prophet/](url). Meanwhile, for the geography-oriented analysis, in order to quantify the behaviour of a group of nation in Europe, Asia and America during the pandemic we used a method that does dimensionality reduction on the time serie of the given gases (embedding). This is done by using a Neural Network Autoencoder, which is basically a perceptron that tries to create an output which is equal to it's input. We trained the NN and we got the output on the intemediate layer of it (in our work it is 7/9-dimensional).  We then "compressed" the whole time serie in a single vector, which is the internal reppresentation that the NN has of the input. We then combined the different vectors given by every time serie for a given country (one for every gas) by joining them. In the end DBScan is used to clusterize the results, by doing PCA.

# Objectives
Out aim is to create a feasible application to the EODashboard in order to quantify the socio-economic impacts that the pandemic has had on different cuntries. We perform using different varibles from the Copernicus Sentinel 5. In particular we employed SO2, NO2, O3, CO and CH4 event though more variables can be added to further improve our work.

# How to Use

All the notebooks used for the analysis in this competition are in the folder notebook. Since the time was tight some errors can be found. If you find any, let us know and we will be happy to fix it for you. 
Here the list of the main important libraries employed:
- xcube_sh: needed to retrieve data. In order to used this library you have to install xcube. Follow the instruciont dispplye here: [https://github.com/dcs4cop/xcube-sh](url) (Note that you need to create a sentinel-hub or data-cube account in order to retrieve data);
- numpy,pandas to manage data;
- pickle: used to save the data on files;
- kneed;
- keras, tensorflow: used to perform the NN.

We used the following pipeline in order to perform our analysis:
- S5PL2.ipynb: retrieve data and save them in the "data/data_countries" folder;
- merge_files.ipynb: take all the previously files and merge them in two files. Ones with all the Nan values still present while the second one with Nan values managed. These files are saved in the "data/data_merged" directory;
- csv.ipynb: files used to compute the mean over the pre covid period and the covid one. It save these values in the "data/csv" folder. These data will be then plotted in the map.html.
 
Different type of analysis can be done at this point: an autoencoder architecture to reduce time series to a bunch of scalar values representing emission changes during a given period; such scalar values are then be used to differentiate between countries. Such type of analysis can be further improved in order to obtain a more clear clustering.
- geography-oriented (autoenconder.ipynb):
- time-oriented (prophet_analysis2.ipynb):a country-specific time series study to understand the change in emission pattern during the pandemic.

# Map

The map folder contains the useful files in order to visualise the results. The html file is the final result, while the source code is in the python notebook. The data are stored in the data folder. Such map is used as a possible exampe for the implementation of the EODashboard. 
