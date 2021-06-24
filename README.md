# EOChallenge
source: [https://www.eodashboardhackathon.org/](url)

This repository collects materials for the **Earth Observation (EO) Dashboard Hackathon 2021**. Our chosen topic is **_"A comparative analysis"_**.

# The Challenge
source: [https://www.eodashboardhackathon.org/challenges/interconnected-earth-system-impact/comparative-analysis/details](url)

The COVID-19 pandemic has had different impacts in different regions of the world. Your challenge is to perform a comparative analysis of the pandemic’s economic impacts in urban areas for the USA, Asia, and Europe using the EO Dashboard.

# Background
The COVID-19 pandemic has had different impacts in different regions of the world, and these impacts depend on a number of different factors. Your challenge is to perform a comparative analysis of the pandemic’s economic impacts in urban areas for the USA, Asia, and Europe using the EO Dashboard. Your analysis may focus on air quality impact assessment (greenhouse gas, GHG, and NO2) and/or economic impact assessment using simple proxy indicators derived from EO data. You may determine this for a representative and strategically selected sample of areas-of-interest, comparing the impact between two continents.

# Objectives
Can you develop 2-3 globally applicable “proxies” that characterize the impact of the pandemic on air quality and/or socio-economic activities? How can you integrate different proxies into an integrated economic indicator? Use Earth observation data from at least two of the three regions for the developed proxies, ensuring the same assessment can be performed in the USA/Europe/Asia.

# Potential Considerations
How can you develop an integrated economic composite indicator by integrating air quality / air pollution and/or the developed proxies comparatively across the study regions in the US, Europe, and Asia including Japan?

The economic composite indicator may integrate several proxy variables/layers/indicators that can be generated in a consistent way over several regions.
Focus your investigation on selected aspects of the socio-economic system with relevance to pandemic-related impacts (e.g., air quality, public health, commercial retail, transport, etc.)
For each region (i.e., Asia, Europe, USA), ensure that a representative subset of areas is being monitored in your analysis.
Consider demonstrating (1) how your composite indicator performs in quantifying the economic impacts over time, and (2) how your composite indicator differs across the three study regions?　
Examples for indicator proxies may include:
Sentinel-1 and/or ALOS-2 SAR sensors provide highly routine and consistent backscatter measurements at 3m resolution (ALOS-2 selected city) or 10m resolution (Sentinel-1 and ALOS-2), and variations in backscatter in different local time (600 and 1800 by Sentinel-1 and 1200 and 2400 by ALOS-2) can be used as a proxy for the number of parked cars in large parking areas (e.g., shopping malls, factories, airports, stadiums, ports, etc.).
Slowdown Proxy Maps (SPM) and COVID-19 Recovery Proxy Maps (RPM) for 100 cities around the world utilize ESA Sentinel-1 and JAXA ALOS-2 imagery to detect changes in human activity associated with COVID-19 closures/slowdown, as well as track changes in human activity as economic activity begins to resume.
EO Nightlight datasets such as those provided by the Visible and Infrared Imaging Suite (VIIRS) provide a complementary view, as they measure the variation in artificial illumination.
On the other hand, because of decreasing economic activity caused by lockdown/shutdown, the decrease in anthropogenic activities equating to the decrease in GHG CO2 and CH4 by OCO-2 and GOSAT and pollutants NO2 by TOPOMI and OMI from power plants, factory, oil & coal mining and transport are detected.
You may use open source maps such as (but not limited to) OpenStreetMap (OSM) to delineate relevant areas in different categories and create a representative sample of these areas for the three study regions. For example, the OSM Overpass API allows extracting the 50 largest retail, healthcare or other sites and their associated parking lots. Here categories (e.g., “health care facility”) and subtypes (e.g., “health care facility” > “parking lot”) can be queries programmatically using the OSM APIs.
You may potentially integrate additional data sources (e.g., social mobility data, other statistical datasets) to strengthen and validate the proxies or the composite indicator.
Keyword search: social mobility data
