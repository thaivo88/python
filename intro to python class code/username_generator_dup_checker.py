#Import Section

from datetime import date   #import this for Date
import getpass              #import this for User

#Flower Box Section

#########################################################
#                                                       
#   Name:  Thai Vo                          
#   Date:  02/06/2022
#   Program Description:
#
#   Asking users to input employee's first, last name and
#   birth year to create a unique username.
#   Then check for duplicate, if there is a duplicate
#   username then change the username format
#                                                       
#########################################################


#Variables section

    #All variables needed for will be declared here

fname = ""
lname = ""
birthyr = ""
employee_info = []
yn = ""
ylist = ["yes", "Yes", "YES", "Y", "y"]
un_list = []
employee_dict = {}

#Functions section

    #Starting on project 4 all functions created will be in this section


#Input section
    
    #All input logic will be in this section
    #Make sure to use line comments to fully explain the inputs

print("Please enter at least 5 employees informations \nInclude at least 2 employees with same first initial in their first name and same last name and same birth year.")
while len(employee_info) < 5:                                                                           # a loop len of 5
    fname = input("Enter employee's first name: ")                                                      # asking user to input a first name
    while len(fname) < 2:                                                                               # making sure the name is greater than 2 lenght
        fname = input("Enter employee's first name: ")                                                  # asking user to input a first name

    lname = input("Enter employee's last name: ")                                                       # asking user to input a last name
    while len(lname) < 2:                                                                               # making sure the name is greater than 2 lenght
        lname = input("Enter employee's last name: ")                                                   # asking user to input a last name

    birthyr = input("Enter employee's birth year (YYYY): ")                                             # asking user to input a birth year
    while len(birthyr) < 4:                                                                             # making sure the birth year is 4 lenght long
        birthyr = input("Enter employee's birth year (YYYY): ")                                         # asking user to input a birth year

    print("You entered employee " + fname + " " + lname + " " + birthyr + " is this correct? ")         # print statement asking if their entry is correct

    yn = input("Yes or No ")                                                                            # ask the user to input yes or no

    if(yn in ylist):                                                                                    # if the user input any format of yes the employee's information is append to the list
        employee_data = (fname, lname, birthyr)                                                         # placing first name, last name, birth year into a list
        employee_info.append(employee_data)                                                             # adding and appending each set into the list 
        fname = ""
        lname = ""
        birthyr = ""
    else:                                                                                               # when user input NO the variable is cleared out so the user can redo that input
        fname = ""
        lname = ""
        birthyr = ""
        continue                                                                                        # make the loop go back in the beginning to start that entry over


#Process section

    #All processing of user input and calculations will be in this section
    #Make sure to use line comments to fully explain how the data is being processed

# creating a loop from all the information user's input function to create a username
for employee in employee_info:
    emp_fname = employee[0]                                                         # taking the first name from the 3 information from user's input function
    emp_lname = employee[1]                                                         # taking the last name from the 3 information from user's input function
    emp_birthyr = employee[2]                                                       # taking the birth year of the 3 information from user's input function

    un_first_init = emp_fname[0].lower()                                            # taking the index of employee"s first name from the list in lower case
    un_lname = emp_lname.lower()                                                    # taking employee's last name in lower case
    un_birthyr_2d = emp_birthyr[-2] + emp_birthyr[-1]                               # taking the employee's birth year last two index

    username = un_first_init + un_lname + un_birthyr_2d                             # concat employee's first inital, last name, and last two digial of birth year as the username

# a if-else function checking if there is a duplicate username
# if there is a duplicate username to use a different format
    if username in un_list:       
        username = emp_fname.lower() + emp_lname[0].lower() + un_birthyr_2d         # new username format to use full employee's first name, first initial of last name and 2 last digit of birth year
        un_list.append(username)                                                    # append new username to the list
    else:
        un_list.append(username)                                                    # append new username to the list

    employee_dict[username] = employee                                              # creating a dictionary using the username as the key and the 3 information as the value

un_list_cp = list(un_list)                                                          # copying the username list
un_list_cp.sort()                                                                   # sorting the copied username list
    

#Output section

    #Your Username and Today's Date will be in this section and ALWAYS First
    #All output in the form of print functions will be in this section
    #Make sure to use line comments to fully explain what is being displayed and how it is formatted

print(getpass.getuser())                # output username
print(date.today())                     # output today's date
print(employee_info)                    # output of employee data list from users input function
print(un_list)                          # list of username
print(employee_dict)                    # dictionary of employee data
print(un_list_cp)                       # list of username that been sorted


# EOF
