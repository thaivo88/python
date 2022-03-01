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
The indent=4 argument tells dump() to format the data using indentation that matches the data’s structure.


