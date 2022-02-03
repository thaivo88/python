#Import Section

from datetime import date   #import this for Date
import getpass              #import this for User

#Flower Box Section

#########################################################
#                                                       
#   Name:  Thai Vo                          
#   Date:  01/30/2022
#   Program Description:
#
#   username_generator.py assignment module 1 of week 2
#   In this script using list, tuple, set, and dirctionary
#   to generate a username for a set of information about
#   an employee given their name and birth year
#                                                       
#########################################################

#Variables section

    #All variables needed for will be declared here

#Functions section

    #Starting on project 4 all functions created will be in this section

#Input section
    
    #All input logic will be in this section
    #Make sure to use line comments to fully explain the inputs

    # creating a list of employees first name
employees_first = ["Dale", "Debbie", "John", "Dave", "Mike"]
    # creating a list of employees last name
employees_last = ["Fontenot", "Fontenot", "Doe", "Dane", "Roberts"] 
    # creating a list of employees birth year
employees_birth = ["1963", "1963", "1965", "1966", "1967"] 

#Process section

    #All processing of user input and calculations will be in this section
    #Make sure to use line comments to fully explain how the data is being processed

    # creating a variable to join the 3 lists 
employees_joint_info = zip(employees_first, employees_last, employees_birth)
employees_joint_info2 = zip(employees_first, employees_last, employees_birth)

    # creating a blank variable for a list of usernames
usernames = []
    # creating a blank variable for a dictionary to combine the employee's username and information
employees_info = {}
    # creating a blank variable for a list to combine the employee's username and information
total_emp_info = []

    # creating a loop statement in range of 1 - 5
for count in range(0,5):
    name_first = employees_first[count].lower()                                     # taking the index of employee"s first name from the list in lower case
    first_init = name_first[0]                                                      # taking the first letter of the employee's first name
    last_name = employees_last[count].lower()                                       # taking the index of employee"s last name from the list in lower case
    birth_yr1 = employees_birth[count]                                              # taking the index of employee"s birth year from the list
    birth_yr2 = birth_yr1[-2] + birth_yr1[-1]                                       # stripping the birth year down to the last two digit
    username = first_init + last_name + birth_yr2                                   # creating a username by concat the first initial, last name, and last two digitl of birth year
    usernames.append(username)                                                      # appending username to the usernames list
    employees_info = {                                                              # making the dictionary to contain username : first name, last name, birth year
        username : "(" + name_first + ", " + last_name + ", " + birth_yr1 + ")"
    }
total_emp_info = dict(zip(usernames,employees_joint_info))                          # joining username and employees information and turing it into a dictionary
set(usernames)                                                                      # removing any duplicate
list(usernames)                                                                     # reverting the set back into a list



unique_username = []                            # creating a blank list for the loop
for unique in usernames:                        # creating a loop statement from the usernames list for each username
    unique_username.append(unique)              # appending each username into the list
unique_username = set(unique_username)          # removing any duplicate


#Output section

    #Your Username and Today's Date will be in this section and ALWAYS First
    #All output in the form of print functions will be in this section
    #Make sure to use line comments to fully explain what is being displayed and how it is formatted


print(getpass.getuser())                # output username
print(date.today())                     # output today's date
print(tuple(employees_joint_info2))      # output the joint list/zip
print(usernames)                        # output the username list
print(set(usernames))                   # output username set
print(unique_username)                  # output username list with no duplicate
print(total_emp_info)                   # employee data dictionary
print(sorted(usernames))                # sorted list of username


#EOF
