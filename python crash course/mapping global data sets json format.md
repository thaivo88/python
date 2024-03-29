json file for earthquake data
```
{"type":"FeatureCollection","metadata":{"generated":1550361461000,...
{"type":"Feature","properties":{"mag":1.2,"place":"11km NNE of Nor...
{"type":"Feature","properties":{"mag":4.3,"place":"69km NNW of Ayn...
{"type":"Feature","properties":{"mag":3.6,"place":"126km SSE of Co...
{"type":"Feature","properties":{"mag":2.1,"place":"21km NNW of Teh...
{"type":"Feature","properties":{"mag":4,"place":"57km SSW of Kakto...
--snip--
```
loading the data and displaying it in a format that’s easier to read.
```
import json
# Explore the structure of the data.
filename = 'data/eq_data_1_day_m1.json'
with open(filename) as f:
  all_eq_data = json.load(f)
readable_file = 'data/readable_eq_data.json'
with open(readable_file, 'w') as f:
  json.dump(all_eq_data, f, indent=4)
```
json file now is more readable
```
{
"type": "FeatureCollection",
"metadata": {
  "generated": 1550361461000,
  "url": "https://earthquake.usgs.gov/earthquakes/.../1.0_day.geojson",
  "title": "USGS Magnitude 1.0+ Earthquakes, Past Day",
  "status": 200,
  "api": "1.7.0",
  "count": 158
},
"features": [
--snip--
```
The <i>indent=4</i> argument tells <i>dump()</i> to format the data using indentation that matches the data’s structure.
<b>"metadata"</b> This tells us when the data file was generated and where we can find the data online
This <b>geoJSON</b> file has a structure that’s helpful for location-based data.



Using the list containing data about each earthquake, we can loop through that list and extract any information we want. Now we’ll pull the magnitude of each earthquake.
```
--snip--
all_eq_dicts = all_eq_data['features']
mags = []
for eq_dict in all_eq_dicts:
  mag = eq_dict['properties']['mag']
  mags.append(mag)
print(mags[:10])
--------- Output ---------
[0.96, 1.2, 4.3, 3.6, 2.1, 4, 1.06, 2.3, 4.9, 1.8]
```


Extracting Location Data
The location data is stored under the key "geometry". Inside the geometry dictionary is a "coordinates" key, and the first two values in this list are the longitude and latitude.
```
--snip--
all_eq_dicts = all_eq_data['features']
mags, lons, lats = [], [], []
for eq_dict in all_eq_dicts:
  mag = eq_dict['properties']['mag']
  lon = eq_dict['geometry']['coordinates'][0]
  lat = eq_dict['geometry']['coordinates'][1]
  mags.append(mag)
  lons.append(lon)
  lats.append(lat)
print(mags[:10])
print(lons[:5])
print(lats[:5])
--------- Output ---------
[0.96, 1.2, 4.3, 3.6, 2.1, 4, 1.06, 2.3, 4.9, 1.8]
[-116.7941667, -148.9865, -74.2343, -161.6801, -118.5316667]
[33.4863333, 64.6673, -12.1025, 54.2232, 35.3098333]
```


Building a World map
With plotly, a geo map of the world can be use with coordinates as x (longitudes) and y (latitudes) axis
```
import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline
--snip--
for eq_dict in all_eq_dicts:
--snip--
Map the earthquakes.
data = [Scattergeo(lon=lons, lat=lats)]
my_layout = Layout(title='Global Earthquakes')
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')
```
--------- Output ---------

![image](https://user-images.githubusercontent.com/15881158/156099918-e1c0f28d-6da8-45fb-9306-cf43e4d91b0a.png)


Customizing Marker Size
Plotly offers a huge variety of customizations you can make to a data series, each of which can be expressed as a key-value pair. Here we’re using the key 'marker' to specify how big each marker on the map should be.
```
import json
--snip--
# Map the earthquakes.
data = [{
  'type': 'scattergeo',
  'lon': lons,
  'lat': lats,
  'marker': {
    'size': [5*mag for mag in mags],
  },
}]
my_layout = Layout(title='Global Earthquakes')
--snip--
```
--------- Output ---------

![image](https://user-images.githubusercontent.com/15881158/156221673-6f646962-db2e-42d6-9f5b-783a2e9bed3d.png)


Customizing Marker Colors
We can also customize each marker’s color to provide some classification to the severity of each earthquake. We’ll use Plotly’s colorscales to do this.
```
--snip--
filename = 'data/eq_data_30_day_m1.json'
--snip--
# Map the earthquakes.
data = [{
--snip--
  'marker': {
    'size': [5*mag for mag in mags],
    'color': mags,
    'colorscale': 'Viridis',
    'reversescale': True,
    'colorbar': {'title': 'Magnitude'},
  },
}]
--snip--
```
--------- Output ---------

![image](https://user-images.githubusercontent.com/15881158/156270149-88f01c5f-eae1-43e0-96e4-00501cfdc0f4.png)

We use the <i>mags</i> list to determine the color that’s used.

The <i>'colorscale'</i> setting tells Plotly which range of colors to use: 'Viridis' is a colorscale that ranges from dark blue to bright yellow and works well for this data set.

We set <i>'reversescale'</i> to True, because we want to use bright yellow for the lowest values and dark blue for the most severe earthquakes.

The <i>'colorbar'</i> setting allows us to control the appearance of the colorscale shown on the side of the map. Here we title the colorscale 'Magnitude' to make it clear what the colors represent.




Other Colorscales
```
from plotly import colors
for key in colors.PLOTLY_SCALES.keys():
  print(key)
--------- Output ---------
Greys
YlGnBu
Greens
--snip--
Viridis
```



Adding Hover Text
To finish this map, we’ll add some informative text that appears when you hover over the marker representing an earthquake. In addition to showing the longitude and latitude, which appear by default, we’ll show the magnitude and provide a description of the approximate location as well.
```
--snip--
mags, lons, lats, hover_texts = [], [], [], []
for eq_dict in all_eq_dicts:
  --snip--
  lat = eq_dict['geometry']['coordinates'][1]
  title = eq_dict['properties']['title']
  mags.append(mag)
  lons.append(lon)
  lats.append(lat)
  hover_texts.append(title)
--snip--
# Map the earthquakes.
data = [{
  'type': 'scattergeo',
  'lon': lons,
  'lat': lats,
  'text': hover_texts,
  'marker': {
--snip--
  },
}]
--snip--
```


We first make a list called <i>hover_texts</i> to store the label we’ll use for each marker. The “title” section of the earthquake data contains a descriptive name of the magnitude and location of each earthquake in addition to its longitude and latitude. we pull this information and assign it to the variable <i>title</i>, and then append it to the list <i>hover_texts</i>.
