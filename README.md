# The Challenge
source: [https://www.eodashboardhackathon.org/challenges/interconnected-earth-system-impact/comparative-analysis/details](url)

The COVID-19 pandemic has had different impacts in different regions of the world. Your challenge is to perform a comparative analysis of the pandemic’s economic impacts in urban areas for the USA, Asia, and Europe using the EO Dashboard.

# Background
2020: under the pandemic wave, the world slowed down. Industries and transports were heavily impacted and beyond the effects on private lives and social interactions, the pandemic had repercussions on the environment. The question leading us was how much of these changes we could actually see in data from satellite. We focused on variations in greenhouse gases (SO2, NO2, O3, CO) and ozone, and on the differences of these variations across different world countries. To this end we performed a time-oriented analysis on time series and a complementary geography-oriented analysis, based on unsupervised feature extracting, to highlight differences between countries.

# Data analysis
In order to quantify the behaviour of a group of nation in Europe, Asia and America during the pandemic we used a method that does dimensionality reduction on the time serie of the given gases. This is done by using a Neural Network Autoencoder, which is basically a perceptron that tries to create an output which is equal to it's input. We trained the NN and we got the output on the intemediate layer of it (in our work it is 7-dimensional). We then "compressed" the whole time serie in a single vector, which is the internal reppresentation that the NN has of the input. We then combined the different vectors given by every time serie for a given country (one for every gas) by joining them. In the end DBScan is used to clusterize the results, optionally by doing PCA.

# Objectives
Out aim is to create a feasible application to the EODashboard in order to quantify the socio-economic impacts that the pandemic has had on different cuntries. We perform using different varibles from the Copernicus Sentinel 5. 

# How to Use

- First of all data must be retreived from Sentinel hub platform by using the file: S5PL2.ipynb
- After that the data for all the countries must be stored using the merge_file.ipybn
- Different type of analysis can be done at this point:

  a) An autoencoder architecture to reduce time series to a bunch of scalar values representing emission changes during a given period; such scalar values    could then be used to differentiate between countries.
  
  b) A country-specific time series study to understand the change in emission pattern during the pandemic. This is achieved by using Prophet [https://github.com/facebook/prophet](url), open source software released by Facebook's Core Data Science team.

