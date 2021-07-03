import folium
import os
import json
import pandas as pd
import pickle
import base64
from folium import IFrame
from os import listdir
from os.path import isfile, join

m = folium.Map(location=[42.3601, -71.0589], zoom_start=3)

states = os.path.join('data', 'countries.json')

#CH4_data = pd.read_csv(os.path.join('data', 'CH4.csv'))
#O3_data = pd.read_csv(os.path.join('data', 'O3.csv'))
#NO2_data = pd.read_csv(os.path.join('data', 'NO2.csv'))
#CO_data = pd.read_csv(os.path.join('data', 'CO.csv'))
#SO2_data = pd.read_csv(os.path.join('data', 'SO2.csv'))
index_data = pd.read_csv(os.path.join('data', 'seven.csv'))

folium.Choropleth(
    geo_data=states,
    name='index',
    data=index_data,
    columns=['State', 'cluster'],
    key_on='feature.id',
    fill_color='PuRd',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='Index'
).add_to(m)

tooltip = 'Click For More Info'
html = '<img src="data:image/png;base64,{}">'.format
png = 'img/ITA.png'
encoded = base64.b64encode(open(png, 'rb').read())
iframe = IFrame(html(encoded.decode('UTF-8')), width=1188, height=500)
popup = folium.Popup(iframe, max_width=3000)
#icon = folium.Icon(color="blue", icon="ok")

f=open(states)
data=json.load(f)
onlyfiles = [f for f in listdir('img/') if isfile(join('img/', f))]
onlyfiles.remove('.DS_Store')

for file in onlyfiles:
    name=file.replace('.png','')
    png = 'img/'+name+'.png'
    encoded = base64.b64encode(open(png, 'rb').read())
    iframe = IFrame(html(encoded.decode('UTF-8')), width=1188, height=500)
    popup = folium.Popup(iframe, max_width=3000)
    for i in range(0, len(data['features'])):
        if data['features'][i]['id']==name:

            if len(data['features'][i]['geometry']['coordinates'])>1:
                for a in range(0,len(data['features'][i]['geometry']['coordinates'])):
                    gj = folium.GeoJson(data={"type": "Polygon", "coordinates":data['features'][i]['geometry']['coordinates'][a]})
                    gj.add_child(folium.Popup(iframe, max_width=3000))
                    gj.add_to(m)
            else:
                gj = folium.GeoJson(data={"type": "Polygon", "coordinates":data['features'][i]['geometry']['coordinates']})
                gj.add_child(folium.Popup(iframe, max_width=3000))
                gj.add_to(m)




folium.LayerControl().add_to(m)



m.save('map.html')
