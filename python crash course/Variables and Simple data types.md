Python interpreter - reads through the program and determines what each word in the program means.
Syntax highlighting - displays different phrase in different color for easy reading and coding.
Traceback - is a record of where the interpreter ran into trouble when trying to execute your code. 
The interpreter provides a traceback when a program cannot run successfully. 

When you’re using variables in Python, you need to adhere to a few rules and guidelines:

- Variable names can contain only letters, numbers, and underscores. They can start with a letter or an underscore, but not with a 
number. For instance, you can call a variable message_1 but not 1_message.
-Spaces are not allowed in variable names, but underscores can be used to separate words in variable names. For example, 
greeting_message works, but greeting message will cause errors.
-Avoid using Python keywords and function names as variable names; that is, do not use words that Python has reserved for a particular 
programmatic purpose, such as the word print. (See “Python Keywords and Built-in Functions” on page 471.)
-   Variable names should be short but descriptive. For example, name is better than n, student_name is better than s_n, and name_length 
is better than length_of_persons_name.
- Be careful when using the lowercase letter l and the uppercase letter O because they could be confused with the numbers 1 and 0.

* Uppercase letters in variable names have special meanings

A string is a series of characters. Anything inside quotes is considered a string in Python, and you can use single or double quotes. 


code:
```
---------------------
name = "ada lovelace"
print(name.title())
---------------------
```
output:
```
---------------------
Ada Lovelace
---------------------
```
A method is an action that Python can perform on a piece of data. The dot (.) after name in name.title() tells Python to make the title() 
method act on the variable name.

Every method is followed by a set of parentheses, because methods often need additional information to do their work.



code:
```
------------------------------------------
first_name = "ada"
last_name = "lovelace"
 full_name = f"{first_name} {last_name}"
print(full_name)
------------------------------------------
```
```
output:
------------------------------------------
ada lovelace
------------------------------------------
```
To insert a variable’s value into a string, place the letter f immediately before the opening quotation mark. Put braces around 
the name or names of any variable you want to use inside the string. Python will replace each variable with its value when the 
string is displayed.

These strings are called f-strings. The f is for format, because Python formats the string by replacing the name of any variable 
in braces with its value.

In programming, whitespace refers to any nonprinting character, such as spaces, tabs, and end-of-line symbols. 
You can use whitespace to organize your output so it’s easier for users to read.
```
/t - tab
/n - new line
```

Extra whitespace can be confusing in your programs. To programmers 'python' and 'python ' look pretty much the same. 
But to a program, they are two different strings. Python detects the extra space in 'python ' and considers it significant 
unless you tell it otherwise.

Python uses two multiplication symbols to represent exponents
Python supports the order of operations too, so you can use multiple operations in one expression. 
You can also use parentheses to modify the order of operations so Python can evaluate your expression in the order you specify.

floats - any number with a decimal point

When you divide any two numbers, even if they are integers that result in a whole number, you’ll always get a float
```
>>> 4/2
2.0
```
If you mix an integer and a float in any other operation, you’ll get a float as well
```
>>> 1 + 2.0
3.0
>>> 2 * 3.0
6.0
>>> 3.0 ** 2
9.0
```

Python defaults to a float in any operation that uses a float, even if the output is a whole number.

When you’re writing long numbers, you can group digits using underscores to make large numbers more readable:
```
>>> universe_age = 14_000_000_000
```
When you print a number that was defined using underscores, Python prints only the digits:
```
>>> print(universe_age)
14000000000
```
Python ignores the underscores when storing these kinds of values. Even if you don’t group the digits in threes, the value 
will still be unaffected.



You can assign values to more than one variable using just a single line.
This can help shorten your programs and make them easier to read.
```
>>> x, y, z = 0, 0, 0
```
You need to separate the variable names with commas, and do the same with the values, and Python will assign each value to its 
respectively positioned variable.


Constant = is like a variable whose value stays the same throughout the life of a program.
* Python doesn’t have built-in constant types, but Python programmers use all capital letters to indicate a variable should be 
treated as a constant and never be changed. 
When you want to treat a variable as a constant in your code, make the name of the variable all capital letters.








