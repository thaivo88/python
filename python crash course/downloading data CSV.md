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

The <i>reader</i> object processes the first line of comma-separated values in the file and stores each as an item in a list.
The csv module contains a <i>next()</i> function, which returns the next line in the file when passed the reader object. In the preceding listing, we call <i>next()</i> only once so we get the first line of the file, which contains the file headers.

