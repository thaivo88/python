Object-oriented programming is one of the most effective approaches to writing software.
In object-oriented programming you write classes that represent real-world things and situations, and you create objects 
based on these classes. When you write a class, you define the general behavior that a whole category of objects can have.

Class names should be written in CamelCase. To do this, capitalize the first letter of each word in the name, 
and don’t use underscores.

Making an object from a class is called instantiation, and you work with instances of a class.
capitalized names refer to classes in Python
```
--------------------------------------------------------------
class Dog:
  """A simple attempt to model a dog."""
  def __init__(self, name, age):
    """Initialize name and age attributes."""
    self.name = name
    self.age = age
    
  def sit(self):
    """Simulate a dog sitting in response to a command."""
    print(f"{self.name} is now sitting.")

  def roll_over(self):
    """Simulate rolling over in response to a command."""
    print(f"{self.name} rolled over!")

my_dog = Dog('Willie', 6)
your_dog = Dog('Lucy', 3)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()

print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()
--------------------------------------------------------------
My dog's name is Willie.
My dog is 6 years old.
Willie is now sitting.

Your dog's name is Lucy.
Your dog is 3 years old.
Lucy is now sitting.
--------------------------------------------------------------
```
A function that’s part of a class is a method. Everything you learned about functions applies to methods as well; 
the only practical difference for now is the way we’ll call methods.
The __init__() method at is a special method that Python runs automatically whenever we create a new instance based
on the Dog class. This method has two leading underscores and two trailing underscores, a convention that helps prevent 
Python’s default method names from conflicting with your method names.
The self parameter is required in the method definition, and it must come first before the other parameters.



Working with classes and instances
You can use classes to represent many real-world situations. Once you write a class, you’ll spend most of your time working 
with instances created from that class.



                                              Modifying attribute values
You can change an attribute’s value in three ways: you can change the value directly through an instance, set the value through 
a method, or increment the value (add a certain amount to it) through a method.

    -Modifying an attribute's value directly
The simplest way to modify the value of an attribute is to access the attribute directly through an instance.
```
[instance].[attribute] = [value]
```

    -Modifying an Attribute’s Value Through a Method
It can be helpful to have methods that update certain attributes for you. Instead of accessing the attribute directly, 
you pass the new value to a method that handles the updating internally.    
  
    -Incrementing an Attribute’s Value Through a Method
Sometimes you’ll want to increment an attribute’s value by a certain amount rather than set an entirely new value.



                                                        Inheritance
You don’t always have to start from scratch when writing a class. If the class you’re writing is a specialized version of another 
class you wrote, you can use inheritance. When one class inherits from another, it takes on the attributes and methods of the 
first class. The original class is called the parent class, and the new class is the child class. The child class can inherit any
or all of the attributes and methods of its parent class, but it’s also free to define new attributes and methods of its own.

When you’re writing a new class based on an existing class, you’ll often want to call the __init__()
method from the parent class. This will initialize any attributes that were defined in the parent __init__() method and make
them available in the child class.

When you create a child class, the parent class must be part of the current file and must appear before the child class in the file.
```
------------------------------------------------------------------
class Car:
  """A simple attempt to represent a car."""

  def __init__(self, make, model, year):
    self.make = make
    self.model = model
    self.year = year
    self.odometer_reading = 0

  def get_descriptive_name(self):
    long_name = f"{self.year} {self.manufacturer} {self.model}"
    return long_name.title()
  
  def read_odometer(self):
    print(f"This car has {self.odometer_reading} miles on it.")

def update_odometer(self, mileage):
    if mileage >= self.odometer_reading:
      self.odometer_reading = mileage
    else:
      print("You can't roll back an odometer!")

  def increment_odometer(self, miles):
    self.odometer_reading += miles

class ElectricCar(Car):
  """Represent aspects of a car, specific to electric vehicles."""

  def __init__(self, make, model, year):
    """Initialize attributes of the parent class."""
    super().__init__(make, model, year)

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
------------------------------------------------------------------
```

The super() function is a special function that allows you to call a method from the parent class. This line tells Python to 
call the __init__() method from Car, which gives an ElectricCar instance all the attributes defined in that method. 
The name super comes from a convention of calling the parent class a superclass and the child class a subclass.



Defining Attributes and Methods for the Child Class:
Once you have a child class that inherits from a parent class, you can add any new attributes and methods necessary to 
differentiate the child class from the parent class.

When you store your classes in several modules, you may find that a class in one module depends on a class in another module.
When this happens, you can import the required class into the first module.










