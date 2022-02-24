functions are named blocks of code that are designed to do one specific job.
modules are where you will store functions in separate files to help organize your main program file

'def' keywork is used in python to inform the program you are defining a function
function definition tells python the name of the function and what kind of information the function needs to do its job.

docstring is a function comment that describe the function does it use triple quotes """Enter Comments"""

parameter is a piece of information the function needs to do its job assigned as a variable
argument is a piece of information that is passed from a function call to a function.
the variable parameter calls on the argument
```
---------------------------------------
def [name_of_function]([parameter]):
  [codes]
---------------------------------------
```
```
---------------------------------------
def greet_user(username):
  """Display a simple greeting."""
  print(f"Hello, {username.title()}!")
  
greet_user('jesse')
---------------------------------------
Hello, Jesse!
---------------------------------------
```
Passing Arguments: function can have multiple parameters to call multiple arguments.
Positional arguments which need to be in the same order the parameters were written
Keyword arguments where each argument consists of a variable name and a value

Positional argument:
```
------------------------------------------------------------
def describe_pet(animal_type, pet_name):
  """Display information about a pet."""
  print(f"\nI have a {animal_type}.")
  print(f"My {animal_type}'s name is {pet_name.title()}.")
  
describe_pet('hamster', 'harry')
------------------------------------------------------------
I have a hamster.
My hamster's name is Harry.
------------------------------------------------------------
```

Keyword argument:
```
------------------------------------------------------------
def describe_pet(animal_type, pet_name):
  """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    
print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet(animal_type='hamster', pet_name='harry')
------------------------------------------------------------
I have a hamster.
My hamster's name is Harry.
------------------------------------------------------------
```

you can define a default value for each parameter. If an argument for a parameter is provided in the function call, Python uses
the argument value. If not, it uses the parameter’s default value.

default value:
```
------------------------------------------------------------
def describe_pet(pet_name, animal_type='dog'):
  """Display information about a pet."""
  print(f"\nI have a {animal_type}.")
  print(f"My {animal_type}'s name is {pet_name.title()}.")
  
describe_pet(pet_name='willie')
------------------------------------------------------------
I have a dog.
My dog's name is Willie.
------------------------------------------------------------
```
If you specify a default value for a parameter, no spaces should be used on either side of the equal sign

The value the function returns is called a return value. The return statement takes a value 
from inside a function and sends it back to the line that called the function.

return value:
```
------------------------------------------------------------
def get_formatted_name(first_name, last_name):
  """Return a full name, neatly formatted."""
  full_name = f"{first_name} {last_name}"
  return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)
------------------------------------------------------------
Jimi Hendrix
------------------------------------------------------------
```


Making an Argument Optional
To make the middle name optional, we can give the middle_name argument an empty defult value and ignore the argument unless the
user provides a value.
```
---------------------------------------------------------------
def get_formatted_name(first_name, last_name, middle_name=''):
  """Return a full name, neatly formatted."""
  if middle_name:
    full_name = f"{first_name} {middle_name} {last_name}"
  else:
    full_name = f"{first_name} {last_name}"
  return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)

---------------------------------------------------------------
Jimi Hendrix
John Lee Hooker
---------------------------------------------------------------
```


Passing a list
```
---------------------------------------------------------------
def greet_users(names):
  """Print a simple greeting to each user in the list."""
  for name in names:
    msg = f"Hello, {name.title()}!"
    print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)
---------------------------------------------------------------
Hello, Hannah!
Hello, Ty!
Hello, Margot!
---------------------------------------------------------------
```

modifying a list in a function
Without function def
```
--------------------------------------------------------------------
# Start with some designs that need to be printed.
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

# Simulate printing each design, until none are left.
# Move each design to completed_models after printing.
while unprinted_designs:
  current_design = unprinted_designs.pop()
  print(f"Printing model: {current_design}")
  completed_models.append(current_design)

# Display all completed models.
print("\nThe following models have been printed:")
for completed_model in completed_models:
  print(completed_model)
--------------------------------------------------------------------
```

with function def
```
--------------------------------------------------------------------
def print_models(unprinted_designs, completed_models):
  """
  Simulate printing each design, until none are left.
  Move each design to completed_models after printing.
  """
  while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)

def show_completed_models(completed_models):
  """Show all the models that were printed."""
  print("\nThe following models have been printed:")
  for completed_model in completed_models:
    print(completed_model)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
--------------------------------------------------------------------
Printing model: dodecahedron
Printing model: robot pendant
Printing model: phone case
The following models have been printed:
dodecahedron
robot pendant
phone 
--------------------------------------------------------------------
```


preventing a function from modifying a list
You can send a copy of a list to a function
function_name(list_name[:])



passing an arbitrary number of arguments
Sometimes you won’t know ahead of time how many arguments a function needs to accept. Fortunately, 
Python allows a function to collect an arbitrary number of arguments from the calling statement.
The asterisk in the parameter name *toppings tells Python to make an empty tuple
```
--------------------------------------------------------------------
def make_pizza(*toppings):
  """Print the list of toppings that have been requested."""
  print(toppings)
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
--------------------------------------------------------------------
('pepperoni',)
('mushrooms', 'green peppers', 'extra cheese')
--------------------------------------------------------------------
```


Mixing positional and arbitrary arguments
If you want a function to accept several different kinds of arguments, the parameter that accepts an arbitrary number 
of arguments must be placed last in the function definition.
```
----------------------------------------------------------------------
def make_pizza(size, *toppings):
  """Summarize the pizza we are about to make."""
  print(f"\nMaking a {size}-inch pizza with the following toppings:")
  for topping in toppings:
    print(f"- {topping}")

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
----------------------------------------------------------------------
Making a 16-inch pizza with the following toppings:
- pepperoni

Making a 12-inch pizza with the following toppings:
- mushrooms
- green peppers
- extra cheese
----------------------------------------------------------------------
```


Using arbitrary keyword arguments
Sometimes you’ll want to accept an arbitrary number of arguments, but you
won’t know ahead of time what kind of information will be passed to the
function. In this case, you can write functions that accept as many key-value
pairs as the calling statement provides.
```
----------------------------------------------------------------------
def build_profile(first, last, **user_info):
  """Build a dictionary containing everything we know about a user."""
  user_info['first_name'] = first
  user_info['last_name'] = last
  return user_info

user_profile = build_profile('albert', 'einstein',
                              location='princeton',
                              field='physics')
print(user_profile)
----------------------------------------------------------------------
{'location': 'princeton', 'field': 'physics',
'first_name': 'albert', 'last_name': 'einstein'}
----------------------------------------------------------------------
```
The definition of build_profile() expects a first and last name, and then it allows the user to pass in as many name-value 
pairs as they want. The double asterisks before the parameter **user_info cause Python to create an empty dictionary called
user_info and pack whatever name-value pairs it receives into this dictionary. Within the function, you can access the key
value pairs in user_info just as you would for any dictionary.



Storing your functions in modules
storing your functions in a separate file called a module and then importing that module into your main program. An
import statement tells Python to make the code in a module available in the currently running program file.
To call a function from an imported module, enter the name of the module you imported followed by the name of the function,
separated by a dot.
```
  module_name.function_name()
```

You can also import a specific function from a module. Here’s the general syntax for this approach:
```  
  from module_name import function_name
```

You can import as many functions as you want from a module by separating each function’s name with a comma:
```
from module_name import function_0, function_1, function_2
```


Using as to give a function as alias
If the name of a function you’re importing might conflict with an existing name in your program or if the function name is long, 
you can use a short, unique alias—an alternate name similar to a nickname for the function. You’ll give the function this special 
nickname when you import the function.
```
  from module_name import function_name as fn
  from pizza import make_pizza as mp
```

You can also provide an alias for a module name. Giving a module a short alias 
```
  import module_name as mn
  import pizza as p
```  
  
importing all functions in a module
You can tell Python to import every function in a module by using the asterisk (*) operator:
```
  from module_name import *
```  
  
