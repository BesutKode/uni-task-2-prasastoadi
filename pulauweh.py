import os
import csv
import codecs
import json
import folium
from folium import plugins

pulau_weh = 'export.geojson'
geo_json_data = json.load(open(pulau_weh))

daftar_sekolah = []
with codecs.open('sekolah.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    for line in reader:
        daftar_sekolah.append(line)

with codecs.open('bandara.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    lat_Bandara, lon_Bandara = list(reader)[0]
    
tipe_sekolah = {'TK' : 'pink',
                'RA' : 'pink',
                'SD' : 'green',
                'MI' : 'green',
                'SMP' : 'blue',
                'MTS' : 'blue',
                'SMA' : 'red',
                'MA' : 'red',
                'SMK' : 'red'}

lat, lon = 5.8396, 95.2961
zoom_start = 12

m = folium.Map(location=[lat, lon], tiles="Stamen Terrain", zoom_start=zoom_start)

plugins.ScrollZoomToggler().add_to(m)

marker_cluster = folium.MarkerCluster().add_to(m)


for loc in daftar_sekolah:
    folium.Marker(
        location=[loc[1], loc[2]],
        popup=loc[0][8:].upper(),
        icon=folium.Icon(color=tipe_sekolah[loc[0][8:].upper()], icon='ok-sign'),
    ).add_to(m)

folium.Marker(
    location=[lat_Bandara, lon_Bandara],
    popup="Bandar Udara Maimun Saleh",
    icon=folium.Icon(color='black', icon='plane')
    ).add_to(m)
folium.GeoJson(geo_json_data).add_to(m)

m.save('index.html')