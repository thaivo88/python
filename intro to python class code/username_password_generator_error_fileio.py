
#Import Section

from datetime import date   #import this for Date
import getpass              #import this for User
import json
import random

#Flower Box Section

#########################################################
#                                                       
#   Name:  Thai Vo                        
#   Date:  02/27/2022
#   Program Description:
#
#   Asking users to input employee's first, last name and
#   birth year to create a unique username.
#   Then check for duplicate, if there is a duplicate
#   username then change the username format
#   asking user for password format to generate unique 
#   password. Adding exception handling
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
em_greet_age_list = []
em_db_dict = {}
em_greet_age = ()
pw_ln_int = 0
use_num_pw = False
use_sp_char_pw = False
error_msg = ""

#Functions section

    #Starting on project 4 all functions created will be in this section

# creating a function to see if there is any duplicate username and if there is use a different formate
def gen_un(firstn, lastn, byr, dup):   
    if(not dup):
        usrname = firstn[0].lower() + lastn.lower() + byr[-2:]
    else:
        usrname = firstn.lower() + lastn[0].lower() + byr[-2:]
    return usrname



def gen_pw(pw_ln_int, use_sp_char_pw, use_num_pw):                                                       
    """a function to create and generate a random password"""

    A_Z = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"         # creating a constain variable with upper and lower character of the alphabet
    SP_CHAR = "!@#$%^&*"                                                 # creating a constain variable with special character
    NUM = "0123456789"                                                   # creating a constain variable with number 0-9
    passwd = ""                                                         # creating an empty variable for a holder for the loop
    count = 0                                                           # starting counter at 0 for the lenght of the password the user input for the loop

    while count < pw_ln_int:
        random_num = random.randrange(0,52,1)               # calling/importing the random class to use range 0-52 in increments of 1
        rand_pw_ch = A_Z[random_num]                        # getting a random number indexing from the line above to get a random character
        passwd = passwd + rand_pw_ch                        # adding random character to password incurments
        rand_pw_ch = ""                                     # clearing out the variable for the next loop
        count = count + 1                                   # adding 1 to count

        if use_sp_char_pw and count < pw_ln_int:           # we want to use the self to diff from each user | if use input they want to use special character and the count loop is less than the password lenght the user input
            random_num = random.randrange(0,8,1)            # get a random number in incurment of 1 with range of 8 b/c we have 8 special character
            rand_sp_pw = SP_CHAR[random_num]                # getting a random number indexing from the line above to get a random special character
            random_num = 0
            passwd = passwd + rand_sp_pw                    # adding random special character to password incurments
            rand_sp_pw = ""                                 # clearing out the variable for the next loop
            count = count + 1                               # adding 1 to count

        if use_num_pw and count < pw_ln_int:          
            random_num = random.randrange(0,10,1)           # get a random number in incurment of 1 with range of 10 b/c we have 10 number character
            rand_num_pw = NUM[random_num]                   # getting a random number indexing from the line above to get a random number character
            random_num = 0
            passwd = passwd + rand_num_pw                   # adding random number character to password incurments
            rand_num_pw = ""                                # clearing out the variable for the next loop
            count = count + 1                               # adding 1 to count
        
    return passwd
    

#Input section

# reading in the txt file data as a dictionary
# added exception handling
try:
    with open("employee_data.txt") as file:
        for line in file:
            txt_file_dict = str(line)
            txt_file_dict = txt_file_dict.replace("\'", "\"")
            em_db_dict = json.loads(txt_file_dict)
except FileNotFoundError:
    print(f"File: {file} not found.")
else:
    file.close()            
    
    #All input logic will be in this section
    #Make sure to use line comments to fully explain the inputs
print("Please enter at 3 employees informations.")
while len(employee_info) < 3:                                                                                                   # a loop len of 3

    while len(fname) < 2 or not fname.isalpha():                                                                                 # making sure the name is greater than 2 lenght or if the name is all letters
        fname = input("Enter employee's first name (Must be all letters) ")                                                      # asking user to input a first name

    while len(lname) < 2 or not lname.isalpha():                                                                                # making sure the name is greater than 2 lenght or if the name is all letters
        lname = input("Enter employee's last name (Must be all letters) ")                                                       # asking user to input a last name

    while len(birthyr) < 4 or not birthyr.isdigit():                                                                            # making sure the birth year is 4 lenght long or if the birth year is all number
        birthyr = input("Enter employee's birth year (Must be 4 digit numbers: YYYY) ")                                         # asking user to input a birth year

    # asking how long the user want their password to be
    # input must be between 6-10 or 16 and check for execption error handling
    while True:                                                                                                                 # loop if true
        print(error_msg)
        pw_ln = input("How long do you want your password? Length must be between 6 and 10 or 16 in length. ")                   # asking user how long they want their password to be
        try:
            pw_ln_int = int(pw_ln)
            if (6 <= pw_ln_int <= 10 or pw_ln_int == 16):
                error_msg = ""
                break
            else:
                error_msg = "Password length isn't a option."
                continue
        except:
            error_msg = "Please enter a whole number between 6 and 10 or 16"
            continue
    
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
    print("You entered employee " + fname + " " + lname + " " + birthyr + " with password length of " + str(pw_ln_int) + ",  to use special characters: " + sp_pw + " and to use numbers: " + num_pw + " is this correct? ")
    yn = input("Yes or No ")

# if the user information is all correct and they stated it correct all the infomration is append to the list
    if(yn in ylist):
        employee_data = (fname, lname, birthyr, pw_ln_int, sp_pw, num_pw)
        employee_info.append(employee_data)
        # clear variables value for next employee
        fname = ""
        lname = ""
        birthyr = ""
        pw_ln_int = 0
        use_sp_char_pw = False
        use_num_pw = False
    # if user input a no then everything is cleared so they can reinput the correct information
    else:
        fname = ""
        lname = ""
        birthyr = ""
        pw_ln_int = 0
        use_sp_char_pw = False
        use_num_pw = False
        continue        

#Process section

    #All processing of user input and calculations will be in this section
    #Make sure to use line comments to fully explain how the data is being processed

# loop each data in the list to set each to a variable
for employee in employee_info:
    emp_fname = employee[0]
    emp_lname = employee[1]
    emp_birthyr = employee[2]
    pw_ln_int = employee[3]
    use_sp_char_pw = employee[4]
    use_num_pw = employee[5]
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

    # building password with the gen_pw function with the given information
    passwd = gen_pw(pw_ln_int, use_sp_char_pw, use_num_pw)

    # creating a list of all information of employee and password
    # then using the username as the key for a dictionary
    em_db = [emp_fname, emp_lname, emp_birthyr, passwd]
    employee_dict[usrname] = em_db

# copying list then sorting it
un_list_cp = list(un_list)
un_list_cp.sort()

# opening file to append user data with expection handling and closing the file
try:
    with open("employee_data.txt" , "a+") as file:
        file.write(str(employee_dict))
except FileNotFoundError:
    print(f"File: {file} not found.")
else:
    file.close()

#Output section

    #Your Username and Today's Date will be in this section and ALWAYS First
    #All output in the form of print functions will be in this section
    #Make sure to use line comments to fully explain what is being displayed and how it is formatted

print(getpass.getuser())                # output username
print(date.today())                     # output today's date
print(employee_info)
print(un_list)
print(employee_dict)
print(un_list_cp)


# EOF