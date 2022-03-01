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

To make it easier to understand the file header data, we print each header and its position in the list:
```
--snip--
with open(filename) as f:
  reader = csv.reader(f)
  header_row = next(reader)
  for index, column_header in enumerate(header_row):
    print(index, column_header)
------------- Output ------------- 
0 STATION
1 NAME
2 DATE
3 PRCP
4 TAVG
5 TMAX
6 TMIN
```
The <i>enumerate()</i> function returns both the index of each item and the value of each item as you loop through a list.

Now we know which columns of data, lets look at TMAX
```
--snip--
with open(filename) as f:
  reader = csv.reader(f)
  header_row = next(reader)
  # Get high temperatures from this file.
  highs = []
  for row in reader:
    high = int(row[5])
    highs.append(high)
print(highs)
------------- Output -------------
[62, 58, 70, 70, 67, 59, 58, 62, 66, 59, 56, 63, 65, 58, 56, 59, 64, 60, 60, 61, 65, 65, 63, 59, 64, 65, 68, 66, 64, 67, 65]
```

Plotting data in a temperature chart
```
import csv
import matplotlib.pyplot as plt
filename = 'data/sitka_weather_07-2018_simple.csv'
with open(filename) as f:
--snip--

# Plot the high temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(highs, c='red')
# Format plot.
plt.title("Daily high temperatures, July 2018", fontsize=24)
plt.xlabel('', fontsize=16)
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()
```
------------- Output -------------

![image](https://user-images.githubusercontent.com/15881158/156084954-fcffe6cc-5d98-4627-a26e-cdd43ce24759.png)



From the list the date is index 2
The data will be read in as a string, so we need a way to convert the string "2018-07-01" to an object representing this date. We can construct an object representing July 1, 2018 using the <i>strptime()</i> method from the <i>datetime</i> module.
```
>>> from datetime import datetime
>>> first_date = datetime.strptime('2018-07-01', '%Y-%m-%d')
>>> print(first_date)
2018-07-01 00:00:00
```

![image](https://user-images.githubusercontent.com/15881158/156085828-1ea35f38-0468-4ff0-a978-edf9d73de366.png)

combining date and high temp
```
import csv
from datetime import datetime
import matplotlib.pyplot as plt
filename = 'data/sitka_weather_07-2018_simple.csv'

with open(filename) as f:
  reader = csv.reader(f)
  header_row = next(reader)
  # Get dates and high temperatures from this file.
  dates, highs = [], []
  for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    high = int(row[5])
    dates.append(current_date)
    highs.append(high)
# Plot the high temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red')
# Format plot.
plt.title("Daily high temperatures, July 2018", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()
```
------------- Output -------------

![image](https://user-images.githubusercontent.com/15881158/156087669-3f69fb6e-12f7-485e-9b63-cd2f0aa3f78a.png)


Plotting two set of data
```
--snip--
filename = 'sitka_weather_2018_simple.csv'
with open(filename) as f:
  reader = csv.reader(f)
  header_row = next(reader)
  # Get dates, and high and low temperatures from this file.
  dates, highs, lows = [], [], []
  for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    high = int(row[5])
    low = int(row[6])
    dates.append(current_date)
    highs.append(high)
    lows.append(low)
# Plot the high and low temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red')
ax.plot(dates, lows, c='blue')
# Format plot.
plt.title("Daily high and low temperatures - 2018", fontsize=24)
--snip--
```
------------- Output -------------

![image](https://user-images.githubusercontent.com/15881158/156088185-10ee67e4-6f7c-4985-b7af-6d1ae1b4d8a7.png)





