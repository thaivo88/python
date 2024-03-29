looping throught the entire list:
Let’s say we have a list of magicians’ names, and we want to print out each name in the list.
```
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
print(magician)
```
```
alice
david
carolina
```



With Python's loop indention matters as all what are indented after the loop will be part of the loop.
Unlike bash or other language where ending a loop with done, or having them in cased in {} ()

This is a logical error. The syntax is valid Python code, but the code does not produce the desired result because a problem 
occurs in its logic.



range:
Python’s range() function makes it easy to generate a series of numbers.
you can use the range() function to print a series of numbers.
The range() function causes Python to start counting at the first value you give it, and it stops when it reaches the second 
value you provide. Because it stops at that second value, the output never contains the end value.
```
for value in range(1, 5):
print(value)
```
```
1
2
3
4
```
You can also pass range() only one argument, and it will start the sequence of numbers at 0. For example,
range(6) would return the numbers from 0 through 5.

** range is like seq in bash **
** for i in $(seq 1 4) **



If you want to make a list of numbers, you can convert the results of range() directly into a list using the list() function.
When you wrap list() around a call to the range() function, the output will be a list of numbers.
```
numbers = list(range(1, 6))
print(numbers)
```
```
[1, 2, 3, 4, 5]
```



We can also use the range() function to tell Python to skip numbers in a given range. If you pass a third argument to range(), 
Python uses that value as a step size when generating numbers.
```
even_numbers = list(range(2, 11, 2))
print(even_numbers)
```
```
[2, 4, 6, 8, 10]
```



A list comprehension allows you to generate this same list in just one line of code. A list comprehension combines the
for loop and the creation of new elements into one line, and automatically appends each new element.
```
squares = []
for value in range(1,11):
  squares.append(value**2)
print(squares)
```
```
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```
```
squares = [value**2 for value in range(1, 11)]        # list comprehension
print(squares)
```
```
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```



slice - working with a group of items in a list.
To make a slice, you specify the index of the first and last elements you want to work with.
As with range(), slicing too starts with 0 and the stop one item before the second index you specify.
```
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
```
```
['charles', 'martina', 'michael']
```
You can include a third value in the brackets indicating a slice. If a third value is
included, this tells Python how many items to skip between items in the specifie range.



To copy a list, you can make a slice that includes the entire original list by omitting the first index and the second index ([:]).
This tells Python to make a slice that starts at the first item and ends with the last item, producing a copy of the entire list.
```
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)
```
```
My favorite foods are:
['pizza', 'falafel', 'carrot cake']
My friend's favorite foods are:
['pizza', 'falafel', 'carrot cake']
```



sometimes you’ll want to create a list of items that cannot change. Tuples allow you to do just that. Python refers to values 
that cannot change as immutable, and an immutable list is called a tuple.
***A tuple looks just like a list except you use parentheses instead of square brackets.***
If you want to define a tuple with one element, you need to include a trailing comma.
***You cannot change any value of an element in a tuple but you can change the whole value of a tuple of the same variable name***
```
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)
dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)
```
```
Original dimensions:
200
50
Modified dimensions:
400
100
```





















