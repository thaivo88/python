dictionaries, which allow you to connect pieces of related information.
A dictionary in Python is a collection of key-value pairs. Each key is connected
to a value, and you can use a key to access the value associated with that key.
A key’s value can be a number, a string, a list, or even another dictionary.
```
------------------------------------------
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])
------------------------------------------
green
5
------------------------------------------
```
A key-value pair is a set of values associated with each other. When you
provide a key, Python returns the value associated with that key. Every key
is connected to its value by a colon, and individual key-value pairs are sepa
rated by commas.



you can add new key-value pairs to a dictionary at any time. You would give the name of the dictionary 
followed by the new key in square brackets along with the new value.
```
-------------------------------------------------------------------
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
-------------------------------------------------------------------
{'color': 'green', 'points': 5}
{'color': 'green', 'points': 5, 'y_position': 25, 'x_position': 0}
-------------------------------------------------------------------
```


To start filling an empty dictionary, define a dictionary with an empty set of braces and then add each key-value
pair on its own line.
```
-------------------------------------
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
-------------------------------------
print(alien_0)
{'color': 'green', 'points': 5}
-------------------------------------
```


modifying values in a dictionary
To modify a value in a dictionary, give the name of the dictionary with the
key in square brackets and then the new value you want associated with that key
```
------------------------------------------------
alien_0 = {'color': 'green'}
print(f"The alien is {alien_0['color']}.")
alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}.")
------------------------------------------------
The alien is green.
The alien is now yellow.
------------------------------------------------
```


track the position of an alien that can move at different speeds. We’ll store a value representing the alien’s
current speed and then use it to determine how far to the right the alien should move
```
-------------------------------------------------------------------
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}")
# Move the alien to the right.
# Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    This must be a fast alien.
    x_increment = 3
# The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New position: {alien_0['x_position']}")
-------------------------------------------------------------------
Original x-position: 0
New x-position: 2
-------------------------------------------------------------------
```


When you no longer need a piece of information that’s stored in a dictionary, you can use the del statement to completely 
remove a key-value pair. All del needs is the name of the dictionary and the key that you want to remove.
```
---------------------------------------------
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
del alien_0['points']
print(alien_0)
---------------------------------------------
{'color': 'green', 'points': 5}
{'color': 'green'}
---------------------------------------------
```


get:
you can use the get() method to set a default value that will be returned if the requested key doesn’t exist.
The get() method requires a key as a first argument. As a second optional argument, you can pass the value to be 
returned if the key doesn’t exist.
```
----------------------------------------------------------------
alien_0 = {'color': 'green', 'speed': 'slow'}
point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)
----------------------------------------------------------------
No point value assigned.
----------------------------------------------------------------
```


Looping Through All Key-Value Pairs:
to write a for loop for a dictionary, you create names for the two variables that will hold the key and value 
in each key-value pair.
items() which returns a list of key-value pairs.
```
----------------------------------------
user_0 = {
  'username': 'efermi',
  'first': 'enrico',
  'last': 'fermi',
  }
for key, value in user_0.items():
  print(f"\nKey: {key}")
  print(f"Value: {value}")
----------------------------------------
Key: last
Value: fermi

Key: first
Value: enrico

Key: username
Value: efermi
----------------------------------------
```


Looping Through All the Keys in a Dictionary:
The keys() method is useful when you don’t need to work with all of the values in a dictionary.
pull all the keys from the dictionary favorite_languages and assign them one at a time to the variable name.
```
----------------------------------------
favorite_languages = {
  'jen': 'python',
  'sarah': 'c',
  'edward': 'ruby',
  'phil': 'python',
  }
for name in favorite_languages.keys():
  print(name.title())
----------------------------------------
Jen
Sarah
Edward
Phil
----------------------------------------
```


You can access the value associated with any key you care about inside the loop by using the current key.
```
-------------------------------------------------------------
favorite_languages = {
  'jen': 'python',
  'sarah': 'c',
  'edward': 'ruby',
  'phil': 'python',
  }
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
  print(name.title())
if name in friends:
    language = favorite_languages[name].title()              # current key = name to pull from favorite_lang 
    print(f"\t{name.title()}, I see you love {language}!")   # and print out the value
-------------------------------------------------------------
Jen.
Sarah.
  Sarah, I see you love C!
Edward.
Phil.
  Phil, I see you love Python!
-------------------------------------------------------------
```


Looping Through a Dictionary’s Keys in a Particular Order:
to do this is to sort the keys as they’re returned in the for loop.
You can use the sorted() function to get a copy of the keys in order.
```
-------------------------------------------------------------
favorite_languages = {
  'jen': 'python',
  'sarah': 'c',
  'edward': 'ruby',
  'phil': 'python',
  }
for name in sorted(favorite_languages.keys()):
  print(f"{name.title()}, thank you for taking the poll.")
-------------------------------------------------------------
Edward, thank you for taking the poll.
Jen, thank you for taking the poll.
Phil, thank you for taking the poll.
Sarah, thank you for taking the poll.
-------------------------------------------------------------
```


Looping Through All Values in a Dictionary:
If you are primarily interested in the values that a dictionary contains,
you can use the values() method to return a list of values without any keys.
```
-------------------------------------------------------------
favorite_languages = {
  'jen': 'python',
  'sarah': 'c',
  'edward': 'ruby',
  'phil': 'python',
  }
print("The following languages have been mentioned:")
for language in favorite_languages.values():
  print(language.title())
-------------------------------------------------------------
The following languages have been mentioned:
Python
C
Python
Ruby
-------------------------------------------------------------
```


set:
To see each language chosen without repetition, we can use a set.
A set is a collection in which each item must be unique
```
-------------------------------------------------------------
favorite_languages = {
  'jen': 'python',
  'sarah': 'c',
  'edward': 'ruby',
  'phil': 'python',
  }
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
  print(language.title())
-------------------------------------------------------------
The following languages have been mentioned:
Python
Dictionaries 105
C
Ruby
-------------------------------------------------------------
```
When you wrap set() around a list that contains duplicate items, Python
identifies the unique items in the list and builds a set from those items.


It’s easy to mistake sets for dictionaries because they’re both wrapped in braces.
When you see braces but no key-value pairs, you’re probably looking at a set. Unlike
lists and dictionaries, sets do not retain items in any specific order.




Sometimes you’ll want to store multiple dictionaries in a list, or a list of
items as a value in a dictionary. This is called nesting. You can nest dictionaries
inside a list, a list of items inside a dictionary, or even a dictionary inside another dictionary.



dictionaries in a list:
```
-------------------------------------------
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
  print(alien)
-------------------------------------------
{'color': 'green', 'points': 5}
{'color': 'yellow', 'points': 10}
{'color': 'red', 'points': 15}
-------------------------------------------
```


list in a dictionary:
```
------------------------------------------------------------
pizza = {
  'crust': 'thick',
  'toppings': ['mushrooms', 'extra cheese'],
  }

print(f"You ordered a {pizza['crust']}-crust pizza "
  "with the following toppings:")
for topping in pizza['toppings']:
  print("\t" + topping)
------------------------------------------------------------
You ordered a thick-crust pizza with the following toppings:
  mushrooms
  extra cheese
------------------------------------------------------------
```


A dictionary in a dictionary:
```
-----------------------------------------------------------
users = {
  'aeinstein': {
    'first': 'albert',
    'last': 'einstein',
    'location': 'princeton',
    },
    
  'mcurie': {
    'first': 'marie',
    'last': 'curie',
    'location': 'paris',
    },
  }

for username, user_info in users.items():
  print(f"\nUsername: {username}")
  full_name = f"{user_info['first']} {user_info['last']}"
  location = user_info['location']
  print(f"\tFull name: {full_name.title()}")
  print(f"\tLocation: {location.title()}")
-----------------------------------------------------------
Username: aeinstein
  Full name: Albert Einstein
  Location: Princeton

Username: mcurie
  Full name: Marie Curie
  Location: Paris
-----------------------------------------------------------  
```

