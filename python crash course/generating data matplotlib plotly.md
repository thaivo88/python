matplotlib = a mathematical plotting library

plotly = creates visulization

```
---------------------------------
import matplotlib.pyplot as plt
squares = [1, 4, 9, 16, 25]
fig, ax = plt.subplots()
ax.plot(squares)
plt.show()
---------------------------------
```
We first import the pyplot module using the alias plt so we don’t have to type pyplot repeatedly.
The pyplot module contains a number of functions that generate charts and plots.

We create a list called squares to hold the data that we’ll plot. Then we follow another common Matplotlib convention by calling the
subplots() function. This function can generate one or more plots in the same figure. The variable fig represents the entire figure 
or collection of plots that are generated. The variable ax represents a single plot in the figure and is the variable we’ll use most 
of the time.

We then use the plot() method, which will try to plot the data it’s given in a meaningful way. The function plt.show() opens 
Matplotlib’s viewer and displays the plot,


```
adding linewidth to change the thickness of the line
  ax.plot(squares, linewidth=3)

Set chart title and label axes.
  ax.set_title("Square Numbers", fontsize=24)
  ax.set_xlabel("Value", fontsize=14)
  ax.set_ylabel("Square of Value", fontsize=14)
Set size of tick labels.
  ax.tick_params(axis='both', labelsize=14)
  
Set the range for each axis.
axis() method requires four values: the minimum and maximum values for the x-axis and the y-axis.
  ax.axis([0, 1100, 0, 1100000])
  
Remove the axes.
  ax.get_xaxis().set_visible(False)
  ax.get_yaxis().set_visible(False)  
```

For the example above the x value is given as default incurrments of 1 starting at 0
if we want to use our own x value we must provide the values
```
providing our own x values
  input_values = [1, 2, 3, 4, 5]
taking our x values to input in plot  
  ax.plot(input_values, squares, linewidth=3)
```  
Matplotlib has many predefined styles available, to check to see what styles availabe on your system run the following:
pyplot.style.available = [pyplot_alias].style.available
```
['Solarize_Light2',
 '_classic_test_patch',
 'bmh',
 'classic',
 'dark_background',
 'fast',
 'fivethirtyeight',
 'ggplot',
 'grayscale',
 'seaborn',
 'seaborn-bright',
 'seaborn-colorblind',
 'seaborn-dark',
 'seaborn-dark-palette',
 'seaborn-darkgrid',
 'seaborn-deep',
 'seaborn-muted',
 'seaborn-notebook',
 'seaborn-paper',
 'seaborn-pastel',
 'seaborn-poster',
 'seaborn-talk',
 'seaborn-ticks',
 'seaborn-white',
 'seaborn-whitegrid',
 'tableau-colorblind10']
 ```
 
To use the style use with pyplot, add the code before the generated code fig, ax = :
```
  pyplot.style.use('[style]')
  plt.style.use('seaborn)        # pyplot alias is plt from the top example
```  
  
To plot a single point, use the scatter() method. Pass the single (x, y) values of the point of interest to scatter()

To plot a series of points, we can pass scatter() separate lists of x- and y- values, like this:
```
  x_values = [1, 2, 3, 4, 5]
  y_values = [1, 4, 9, 16, 25]
  ax.scatter(x_values, y_values, s=100)         # s value is the size of the dot/circle
```


```
using loop to calculate data automatically
  x_values = range(1, 1001)
  y_values = [x**2 for x in x_values]
  ax.scatter(x_values, y_values, s=10)
  
Set the range for each axis.
  ax.axis([0, 1100, 0, 1100000])

To change the color of the points, pass c to scatter() with the name of a color to use in quotation marks
  ax.scatter(x_values, y_values, c='red', s=10)
```

You can also define custom colors using the RGB color model. To defin a color, pass the c argument a tuple with three decimal 
values (one each for red, green, and blue in that order), using values between 0 and 1.  
Values closer to 0 produce dark colors, and values closer to 1 produce lighter colors.
```
ax.scatter(x_values, y_values, c=(0, 0.8, 0), s=10)
```

A colormap is a series of colors in a gradient that moves from a starting to an ending color. You use colormaps in visualizations 
to emphasize a pattern in the data.
We pass the list of y-values to c, and then tell pyplot which colormap to use using the cmap argument. This code colors the points 
with lower y-values light blue and colors the points with higher y-values dark blue.
```
ax.scatter(x_values, y_values, c=y_values, cmap=pyplot.cm.Blues, s=10)
```

If you want your program to automatically save the plot to a file, you can replace the call to pyplot.show() with a call 
to pyplot.savefig():
```
  plt.savefig('squares_plot.png', bbox_inches='tight')
```
The first argument is a filename for the plot image. The second argument trims extra whitespace from the plot. 
If you want the extra whitespace around the plot, just omit this argument.




A random walk is a path that has no clear direction but is determined by a series of random decisions, each of which is 
left entirely to chance.
```
------------------------------------------------------------------------
from random import choice
class RandomWalk:
  """A class to generate random walks."""
  def __init__(self, num_points=5000):
    """Initialize attributes of a walk."""
    self.num_points = num_points
    # All walks start at (0, 0).
    self.x_values = [0]
    self.y_values = [0]
  def fill_walk(self):
  """Calculate all the points in the walk."""
  # Keep taking steps until the walk reaches the desired length.
  while len(self.x_values) < self.num_points:
    Decide which direction to go and how far to go in that direction.
    x_direction = choice([1, -1])    
    x_distance = choice([0, 1, 2, 3, 4])
    x_step = x_direction * x_distance
    y_direction = choice([1, -1])
    y_distance = choice([0, 1, 2, 3, 4])
    y_step = y_direction * y_distance
    Reject moves that go nowhere.
    if x_step == 0 and y_step == 0:
      continue
    # Calculate the new position.
    x = self.x_values[-1] + x_step
    y = self.y_values[-1] + y_step
    self.x_values.append(x)
    self.y_values.append(y)
------------------------------------------------------------------------
import matplotlib.pyplot as plt
from random_walk import RandomWalk
# Make a random walk.
rw = RandomWalk()
rw.fill_walk()
# Plot the points in the walk.
plt.style.use('classic')
fig, ax = plt.subplots()
ax.scatter(rw.x_values, rw.y_values, s=15)
plt.show()
------------------------------------------------------------------------
```




When creating the plot, you can pass a figsize argument to set the size of the figure. The figsize parameter takes a tuple, 
which tells Matplotlib the dimensions of the plotting window in inches.
```
fig, ax = plt.subplots(figsize=(15, 9))
```
if you know your system’s resolution, pass plt.subplots() the resolution using the dpi parameter to set a plot size that
makes effective use of the space available on your screen.
```
fig, ax = plt.subplots(figsize=(10, 6), dpi=128)
```  




rolling a die:
```
------------------------------------------------------------------------
from random import randint
class Die:
    """A class representing a single die."""
    def __init__(self, num_sides=6):
      """Assume a six-sided die."""
      self.num_sides = num_sides
    def roll(self):
      """"Return a random value between 1 and number of sides."""
      return randint(1, self.num_sides)
------------------------------------------------------------------------
from die import Die
Create a D6.
die = Die()
# Make some rolls, and store results in a list.
results = []
for roll_num in range(1000):
  result = die.roll()
  results.append(result)
# Analyze the results.
frequencies = []
for value in range(1, die.num_sides+1):
  frequency = results.count(value)
  frequencies.append(frequency)
print(results)
------------------------------------------------------------------------
[155, 167, 168, 170, 159, 181]
------------------------------------------------------------------------
```



Making a histogram:
With a list of frequencies, we can make a histogram of the results. A histogram is a bar chart showing how often certain 
results occur.
```
------------------------------------------------------------------------
from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die
--snip--
# Analyze the results.
frequencies = []
for value in range(1, die.num_sides+1):
  frequency = results.count(value)
  frequencies.append(frequency)
  
# Visualize the results.
x_values = list(range(1, die.num_sides+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result'}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling one D6 1000 times',
  xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6.html')  
------------------------------------------------------------------------
```

