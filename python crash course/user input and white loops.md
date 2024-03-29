The input() function pauses your program and waits for the user to enter some text. Once Python receives the user’s input, it 
assigns that input to a variable to make it convenient for you to work with.
```
message = input("Tell me something, and I will repeat it back to you: ")
print(message)
```

When you use the input() function, Python interprets everything the user enters as a string. Including numbers so you want to use the
int() to define any number string to integer. We know Python interpreted the input as a string because the number is now 
enclosed in quotes.
The int() function converts a string representation of a number to a numerical representation.


A useful tool for working with numerical information is the modulo operator (%),
which divides one number by another number and returns the remainder:
```
>>> 4 % 3
1
User Input and while Loops 117
>>> 5 % 3
2
>>> 6 % 3
0
>>> 7 % 3
1
```

The for loop takes a collection of items and executes a block of code once for each item in the collection. In contrast, the while
loop runs as long as, or while a certain condition is true. 

flags (condition active or unactive):
For a program that should run only as long as many conditions are true, you can define one variable that determines whether or 
not the entire program is active. This variable, called a flag, acts as a signal to the program. We can write our programs so 
they run while the flag is set to true and stop running when any of several events sets the value of the flag to False.
```
  prompt = "\nTell me something, and I will repeat it back to you:"
  prompt += "\nEnter 'quit' to end the program. "
  
active = True
while active:
    message = input(prompt)
    
    if message == 'quit':
      active = False
    else:
      print(message)
```


break:
To exit a while loop immediately without running any remaining code in the loop, regardless of the results of any conditional test,
use the break statement. The break statement directs the flow of your program; you can use it to control which lines of code are 
executed and which aren’t, so the program only executes code that you want it to, when you want it to.

  prompt = "\nPlease enter the name of a city you have visited:"
  prompt += "\n(Enter 'quit' when you are finished.) "
```
while True:
  city = input(prompt)

  if city == 'quit':
    break
  else:
    print(f"I'd love to go to {city.title()}!")
```
A loop that starts with while True will run forever unless it reaches a break statement. The loop in this program continues asking
the user to enter the names of cities they’ve been to until they enter 'quit'. When they enter 'quit', the break statement runs, 
causing Python to exit the loop.


Continue:
you can use the continue statement to return to the beginning of the loop based on the result of a conditional test. 
For example, consider a loop that counts from 1 to 10 but prints only the odd numbers in that range:
```
current_number = 0
while current_number < 10:
  current_number += 1
  if current_number % 2 == 0:
    continue

print(current_number)
```
First we set current_number to 0. Because it’s less than 10, Python enters the while loop. Once inside the loop, 
we increment the count by 1 so current_number is 1. The if statement then checks the modulo of current_number and 2. 
If the modulo is 0 (which means current_number is divisible by 2), the continue statement tells Python to ignore the rest of
the loop and return to the beginning. If the current number is not divisible by 2, the rest of the loop is executed and 
Python prints the current number.



to keep track of many users and pieces of information, we’ll need to use lists and dictionaries with our while loops.
Using while loops with lists and dictionaries allows you to collect, store, and organize lots of input to examine and 
report on later.

remove() function worked because the value we were interested in appeared only once in the list.















