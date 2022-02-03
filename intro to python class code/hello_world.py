#Import Section
from datetime import date   #import this for Date
import getpass              #import this for User

#Flower Box Section
#########################################################
#                                                       
#   Name:  Thai Vo                          
#   Date:  01/23/2022
#   Program Description:
#
#   hello_world.py assignment module 1 of week 1
#   This python code is to show case my knowledge and 
#   understanding of week 1 concepts of string, numbers,
#   input, variables declaring, index, type, and different
#   functions.
#
#   The follow code will ask the end user to input their 
#   name and ask for a degree of fahrenheith they would
#   like to convert into celsius. The output will return 
#   user's input name and the conversion of fahrenheith 
#   degree into two celsisu: one without decimal and with.
#   
#   Also will print out all the concepts of type, strings,
#   indexing, etc.
#                                                       
#########################################################



#Input section
    #All variables need for use input will be declared here
    #All input functions will be in this section

# Ask user for their name and set it as a variable 
name = input("What is your first name? ")    
# Ask user to input a value for fahrenheit degree for conversion to celsius and set it as a variable                    
f_degree = input("What tempture (in fahrenheit) would you like to convert into Celsius? ")
# converting the variable type from string to float
f_degree = float(f_degree)



#Process section
    #All process of user input and calculations will be in this section

# copy user name and make it all upper case
name_upper = name.upper()
# copy user name and make it all lower case
name_lower = name.lower()
# copy user name and make all leading letter upper case
name_title = name.title()
# count how many characters long the string of the variable is
name_length = len(name)

# indexing the first character of the user name
name_first_initial= name[0]
# indexing the last character of the user name
name_last_initial = name[-1]
# indexing the second to last character of the user name
name_sec_2_last = name[-2]

# using format function to combine a message with variales
message_1 = f"Hello {name_title}, your name is {name_length} characters long!"
# using concatenation function to combine a message with variales
message_2 = "Hello " + name_title + ", your name is " + str(name_length) + " characters long!"

# repeating user name ten times
name_x = name * 10

# Formula: °C = (°F − 32) × 5/9 
# converting fahrenheit degree from user's input value into celsius with integer type
c_degree_int = ( (int(f_degree) - 32) * 5 // 9 )
# same but celsius with float type
c_degree_float =  ( (f_degree - 32) * 5 / 9 )



#Output section

    #Your Username and Today's Date will be in this section and ALWAYS First
    #All output in the form of print functions will be in this section

# output username
print(getpass.getuser())
# output today's date
print(date.today())

# output name entered by user
print(name)
# output type of the name variable 
print(type(name))
# output upper case
print(name_upper)
# output lower case
print(name_lower)
# output first letter in caps
print(name_title)
# output the character length of name variable
print(name_length)
# output the index of the first initial of name variable
print(name_first_initial)
# output the index of the last initial of name variable
print(name_last_initial)
# output the index of the second to last initial of name variable
print(name_sec_2_last)
# output the format function message
print(message_1)
# output the concatenate function message
print(message_2)
# output the degree convertion as a float
print(c_degree_float)
# output the degree convertion as a integer
print(c_degree_int)




# EOF
