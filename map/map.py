import folium
import os
import json
import pandas as pd
import pickle

m = folium.Map(location=[42.3601, -71.0589], zoom_start=3)

states = os.path.join('data', 'countries.json')

CH4_data = state_data = pd.read_csv(os.path.join('data', 'CH4.csv'))
O3_data = pd.read_csv(os.path.join('data', 'O3.csv'))
NO2_data = pd.read_csv(os.path.join('data', 'NO2.csv'))
CO_data = pd.read_csv(os.path.join('data', 'CO.csv'))
SO2_data = pd.read_csv(os.path.join('data', 'SO2.csv'))

folium.Choropleth(
    geo_data=states,
    name='CH4',
    data=CH4_data,
    columns=['Country', 'CH4'],
    key_on='feature.id',
    fill_color='YlGn',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='CH4 Index %'
).add_to(m)

folium.Choropleth(
    geo_data=states,
    name='O3',
    data=O3_data,
    columns=['Country', 'O3'],
    key_on='feature.id',
    fill_color='YlGn',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='O3 Index %'
).add_to(m)

folium.Choropleth(
    geo_data=states,
    name='NO2',
    data=NO2_data,
    columns=['Country', 'NO2'],
    key_on='feature.id',
    fill_color='YlGn',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='NO2 Index %'
).add_to(m)

folium.Choropleth(
    geo_data=states,
    name='CO',
    data=CO_data,
    columns=['Country', 'CO'],
    key_on='feature.id',
    fill_color='YlGn',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='CO Index %'
).add_to(m)

folium.Choropleth(
    geo_data=states,
    name='SO2',
    data=SO2_data,
    columns=['Country', 'SO2'],
    key_on='feature.id',
    fill_color='YlGn',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='SO2 Index %'
).add_to(m)

folium.LayerControl().add_to(m)



m.save('map.html')
