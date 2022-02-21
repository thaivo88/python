
#Import Section

from datetime import date   #import this for Date
import getpass              #import this for User
from person import Person
from employee import Employee


#Flower Box Section

#########################################################
#                                                       
#   Name:  Thai Vo                        
#   Date:  02/20/2022
#   Program Description:
#
#   Asking users to input employee's first, last name and
#   birth year to create a unique username.
#   Then check for duplicate, if there is a duplicate
#   username then change the username format
#   asking user for password format to generate unique 
#   password
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
pw_ln_list = ["10", "11", "12", "13", "14", "15", "16"]
em_greet_age_list = []
em_db_dict = {}
em_greet_age = ()
greet = ""
age = 0

#Functions section

    #Starting on project 4 all functions created will be in this section

# creating a function to see if there is any duplicate username and if there is use a different formate
def gen_un(firstn, lastn, byr, dup):   
    if(not dup):
        usrname = firstn[0].lower() + lastn.lower() + byr[-2:-1]
    else:
        usrname = firstn.lower() + lastn[0].lower() + byr[-2:-1]
    return usrname

#Input section
    
    #All input logic will be in this section
    #Make sure to use line comments to fully explain the inputs
print("Please enter at least 5 employees informations \nInclude at least 2 employees with same first initial in their first name and same last name and same birth year.")
while len(employee_info) < 5:                                                                               # a loop len of 5
    fname = input("Enter employee's first name: ")                                                          # asking user to input a first name
    while len(fname) < 2:                                                                                   # making sure the name is greater than 2 lenght
        fname = input("Enter employee's first name: ")                                                      # asking user to input a first name

    lname = input("Enter employee's last name: ")                                                           # asking user to input a last name
    while len(lname) < 2:                                                                                   # making sure the name is greater than 2 lenght
        lname = input("Enter employee's last name: ")                                                       # asking user to input a last name

    birthyr = input("Enter employee's birth year (YYYY): ")                                                 # asking user to input a birth year
    while len(birthyr) < 4:                                                                                 # making sure the birth year is 4 lenght long
        birthyr = input("Enter employee's birth year (YYYY): ")                                             # asking user to input a birth year

  
    while True:                                                                                                                                     # loop if true
        pw_ln = input("Generating Password; how long would you like the password to be? \nEnter a number between 10 to 16: ")                       # asking user how long they want their password to be
        if pw_ln not in pw_ln_list:                                                                                                                 # if the number the user input is not in the list of 10-16
            pw_ln = ""                                                                                                                              # clear variable
            continue                                                                                                                                # start again and ask them for the length of password
                                                                                                                               
        # if the number is in the list make the number string into a intiger and stop    
        else:                                                                                                                                       
            pw_ln = int(pw_ln)
            break
    
    # asking user if they want special characters in their generated password
    # if their answer is any format of yes then the variable is set to true or no to false
    sp_pw = input("Do you want special characters in your password? y/n: ")
    if sp_pw in ylist:
        use_sp_char_pw = True
    else:
        use_sp_char_pw = False

    # asking user if they want number characters in their generated password
    # if their answer is any format of yes then the variable is set to true or no to false
    num_pw = input("Do you want numbers in your password? ")
    if num_pw in ylist:
        use_num_pw = True
    else:
        use_num_pw = False    

    # print back all the information the user input to see if everything is correct
    print("You entered employee " + fname + " " + lname + " " + birthyr + " with password length of " + str(pw_ln) + ",  to use special characters: " + sp_pw + " and to use numbers: " + num_pw + " is this correct? ")
    yn = input("Yes or No ")

# if the user information is all correct and they stated it correct all the infomration is append to the list
    if(yn in ylist):
        employee_data = (fname, lname, birthyr, pw_ln, sp_pw, num_pw)
        employee_info.append(employee_data)
        # clear variables value for next employee
        fname = ""
        lname = ""
        birthyr = ""
        pw_ln = ""
        sp_pw = False
        num_pw = False
    # if user input a no then everything is cleared so they can reinput the correct information
    else:
        fname = ""
        lname = ""
        birthyr = ""
        pw_ln = ""
        sp_pw = False
        num_pw = False
        continue        

#Process section

    #All processing of user input and calculations will be in this section
    #Make sure to use line comments to fully explain how the data is being processed

# loop each data in the list to set each to a variable
for employee in employee_info:
    emp_fname = employee[0]
    emp_lname = employee[1]
    emp_birthyr = employee[2]
    dup = False

    # providing all the information arguemnt for the gen_un function to generate username
    usrname = gen_un(emp_fname, emp_lname, emp_birthyr, dup)
    
    # test to see if the username isn't in the list of username
    # if there is a duplicate the formation of the username generation will change
    if usrname in un_list:
        dup = True
        usrname = gen_un(emp_fname, emp_lname, emp_birthyr, dup)

    # adding all the username to the list by appending
    un_list.append(usrname)

    # Calling the Employee class for each set of employee
    # Then call the gen_pw function from Employee class to generate password
    employee_list = Employee(employee[0], employee[1], employee[2], employee[3], employee[4], employee[5])
    passwd = employee_list.gen_pw()

    # from the employee list running the function greetings and age from Person class
    # then adding them to the new list
    em_tuple = (employee_list.greetings(), employee_list.age())
    em_greet_age_list.append(em_tuple)

    # creating a list of all information of employee and password
    # then using the username as the key for a dictionary
    em_db = [emp_fname, emp_lname, emp_birthyr, passwd]
    employee_dict[usrname] = em_db



######### removed with function gen_un() #########    
    # moving to function section and recreating as a function def
    # 
    #un_first_init = emp_fname[0].lower()
    #un_lname = emp_lname.lower()
    #un_birthyr_2d = emp_birthyr[-2] + emp_birthyr[-1]
    #
    #username = un_first_init + un_lname + un_birthyr_2d
    # 
    #if username in un_list:
    #    username = emp_fname.lower() + emp_lname[0].lower() + un_birthyr_2d
    #    un_list.append(username)
    #else:
    #    un_list.append(username)

    # employee_dict[username] = employee
#########################################

# copying list then sorting it
un_list_cp = list(un_list)
un_list_cp.sort()

    

#Output section

    #Your Username and Today's Date will be in this section and ALWAYS First
    #All output in the form of print functions will be in this section
    #Make sure to use line comments to fully explain what is being displayed and how it is formatted

print(getpass.getuser())                # output username
print(date.today())                     # output today's date

# a loop for each user to greet and get their age
for em_greet_age in em_greet_age_list:
    greet = em_greet_age[0]
    age = em_greet_age[1]
    print(greet + " You are " + str(age))

print(employee_info)
print(un_list)
print(employee_dict)
print(un_list_cp)


# EOF