import os
import csv
import codecs
import json
import folium
from folium import plugins

pulau_weh = 'export.geojson'
geo_json_data = json.load(open(pulau_weh))

with open('lake.json') as f:
    reader = json.load(f)
    lake_name = reader['name']
    lake_lat = reader['lat']
    lake_lon = reader['lon']

with open('airports.json') as f:
    reader = json.load(f)
    
    for bandara in reader:
        if bandara['iata']=='SBG':
            bandara_name = bandara['name']
            bandara_lat = bandara['lat']
            bandara_lon = bandara['lon']

lat, lon = 5.8396, 95.2961
zoom_start = 12

m = folium.Map(location=[lat, lon], tiles="Stamen Terrain", zoom_start=zoom_start)

plugins.ScrollZoomToggler().add_to(m)

marker_cluster = folium.MarkerCluster().add_to(m)


folium.Marker(
    location=[lake_lat, lake_lon],
    popup=lake_name,
    icon=folium.Icon(color='blue', icon='ok-sign')
    ).add_to(m)

folium.Marker(
    location=[bandara_lat, bandara_lon],
    popup=bandara_name,
    icon=folium.Icon(color='black', icon='plane')
    ).add_to(m)
folium.GeoJson(geo_json_data).add_to(m)

m.save('index.html')