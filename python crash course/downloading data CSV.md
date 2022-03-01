One simple way to store data in a text file is to write the data as a series of values separated by commas, which is called <b>comma-separated values.</b>
Python’s CSV module in the standard library parses the lines in a CSV file and allows us to quickly extract the values we’re interested in.
The first line of the file, which contains a series of headers for the data. These headers tell us what kind of information the data holds.

```
import csv
filename = 'data/sitka_weather_07-2018_simple.csv'
with open(filename) as f:
  reader = csv.reader(f)
  header_row = next(reader)
  print(header_row)
------------- Output -------------  
['STATION', 'NAME', 'DATE', 'PRCP', 'TAVG', 'TMAX', 'TMIN']  
```
