exceptions, which are special objects Python creates to manage errors that arise while a program is running.

json module, which allows you to save user data so it isn’t lost when your program stops running.



```
pi_digits.txt 
--------------------------------------------
3.1415926535
  8979323846
  2643383279
--------------------------------------------
with open('pi_digits.txt') as file_object:
  contents = file_object.read()
print(contents)
--------------------------------------------
```
open() function: you first need to open the file to access it.
The open() function needs one argument: the name of the file you want to open.
open('pi_digits.txt') Python assigns this object to file_object
The keyword with closes the file once access to it is no longer needed.
Once we have a file object representing pi_digits.txt, we use the read() method in the second line of our program to read the 
entire contents of the file and store it as one long string in contents. When we print the value of contents, we get the entire 
text file back.



To be able to read a text file, the file must be in the same directory as your python script 
OR the python script has to be in a parent directory and the text can be in a subdirectory but you must provide the path. - file path
OR it can be anywhwere but you use the file - absolute file path

if absolute file path is too long you can shorten it with a variable:
```
----------------------------------------------------------------------------------------
file_path = '/home/ehmatthes/other_files/text_files/filename.txt'
with open(file_path) as file_object:
----------------------------------------------------------------------------------------
```


When you use with, the file object returned by open() is only available inside the with block that contains it.
if you want to retain access to a file’s contents outside the with block, you can store the file’s lines in a list inside the
block and then work with that list.

the readlines() method takes each line from the file and stores it in a list.





To write text to a file, you need to call open() with a second argument telling Python that you want to write to the file.
```
---------------------------------------------
filename = 'programming.txt'
with open(filename, 'w') as file_object:
  file_object.write("I love programming.")
---------------------------------------------  
```
The call to open() in this example has two arguments. The first argument is still the name of the file we want to open. 
The second argument, 'w', tells Python that we want to open the file in write mode.

You can open a file in read mode ('r'), write mode ('w'), append mode ('a'), 
or a mode that allows you to read and write to the file ('r+'). 
If you omit the mode argument, Python opens the file in read-only mode by default.



![python rwa](https://user-images.githubusercontent.com/15881158/155607243-6cd4fddf-1b71-489d-be7c-98b4c2e7b5a7.PNG)



The open() function automatically creates the file you’re writing to if it doesn’t already exist. However, be careful opening a file 
in write mode ('w') because if the file does exist, Python will erase the contents of the file before returning the file object.

The write() function doesn’t add any newlines to the text you write. So if you write more than one line without including newline 
characters.




If you want to add content to a file instead of writing over existing content, you can open the file in append mode.






                                                            Exceptions

Python uses special objects called exceptions to manage errors that arise during a program’s execution. Whenever an error occurs 
that makes Python unsure what to do next, it creates an exception object. If you write code that handles the exception, the 
program will continue running. If you don’t handle the exception, the program will halt and show a traceback, which
includes a report of the exception that was raised.

Exceptions are handled with try-except blocks. A try-except block asks Python to do something, but it also tells Python what to do
if an exception is raised. When you use try-except blocks, your programs will continue running even if things start to go wrong.


Using try-except blocks
```
--------------------------------------
try:
  print(5/0)
except ZeroDivisionError:
  print("You can't divide by zero!")
--------------------------------------
```
Since you can't divide by zero python run into an error.


```
--------------------------------------
try:
  answer = int(first_number) / int(second_number)
except ZeroDivisionError:
  print("You can't divide by 0!")
else:
  print(answer)
--------------------------------------  
```
Any code that depends on the try block executing successfully goes in the else block.




                                                          json
                                               (JavaScript Object Notation)
                                                          
you’ll almost always want to save the information they entered. A simple way to do this involves storing your data using the
json module. The json module allows you to dump simple Python data structures into a file and load the data from that file the 
next time the program runs.
You can also use json to share data between different Python programs. Even better, the JSON data format is not specific to Python,
so you can share data you store in the JSON format with people who work in many other programming languages.


The json.dump() function takes two arguments: a piece of data to store and a file object it can use to store the data.

```
json.dump
--------------------------------------
import json
numbers = [2, 3, 5, 7, 11, 13]
filename = 'numbers.json'
with open(filename, 'w') as f:
  json.dump(numbers, f)
--------------------------------------
```
```
json.load
--------------------------------------
import json
filename = 'numbers.json'
with open(filename) as f:
  numbers = json.load(f)
print(numbers)
--------------------------------------
```



