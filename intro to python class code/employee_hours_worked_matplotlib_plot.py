#Import Section

from datetime import date   #import this for Date
import getpass              #import this for User
import json                 #import json to use json files
import matplotlib.pyplot as plt     #import matplot to use graph

#Flower Box Section

#########################################################
#                                                       
#   Name:  Thai Vo                        
#   Date:  03/06/2022
#   Program Description:
#
#   using pyplot to create graph to plot the weeks and 
#   hours worked for each employees
#                                                       
#########################################################

#Variables section

    #All variables needed for will be declared here

wk_ending = ""
hrs = 0.0
graph_title = ""
graph_x_label = "Week Ending"
graph_y_label = "Hours Worked"


#Functions section

def display_graph(wk_dates, hrs_worked_per_wk, graph_title, graph_x_label, graph_y_label):
    """function to configuring and displaying a graph"""
    plt.style.use('seaborn-dark')
    plt.plot(wk_dates, hrs_worked_per_wk, linewidth=5)
    # Set chart title and label axes.
    plt.title(graph_title, fontsize=20)
    plt.xlabel(graph_x_label, fontsize=10)
    plt.ylabel(graph_y_label, fontsize=10)
    # Set size of tick labels.
    plt.tick_params(axis="both", labelsize=10)
    plt.show()
    


#Input section

# reading in the txt file data as a dictionary
# added exception handling
try:
    with open("employee_data.txt", "r", encoding="utf-8") as file:
        for line in file:
            txt_file_dict = str(line)
            txt_file_dict = txt_file_dict.strip()
            txt_file_dict = txt_file_dict.replace("\'", "\"")
            employee_dict = json.loads(txt_file_dict)
except FileNotFoundError:
    print(f"File: {file} not found.")
else:
    file.close()            


# loop to username and employee's infomration from the dictionary
for usrname,employee_info in employee_dict.items():
    # setting empty list
    work_dates_ls = []  
    hrs_worked_ls = []

    # looping 4 times to get 4 dates and 4 hours worked
    for x in range(0,4):
        wk_ending = input("Enter a date for week ending for " + usrname + " : ")
        hrs = input("Enter hours worked for " + usrname + " for week ending " + wk_ending + " : ")  
        work_dates_ls.append(wk_ending)
        hrs_worked_ls.append(int(hrs))

#Process section
    #All processing of user input and calculations will be in this section
    #Make sure to use line comments to fully explain how the data is being processed

    # calculating avgerage/min/max
    avg_hrs = sum(hrs_worked_ls) // (len(hrs_worked_ls))
    min_hrs = min(hrs_worked_ls)
    max_hrs = max(hrs_worked_ls)
    # creating a list with the calculations
    work_hrs_stat = [avg_hrs, min_hrs, max_hrs]

    # appending to the dictionary associated with the username for date/hours worked/work hours status
    employee_dict[usrname].append(work_dates_ls) 
    employee_dict[usrname].append(hrs_worked_ls)
    employee_dict[usrname].append(work_hrs_stat)

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

# create graph for each employee and create a table of the week and hours worked.
for usrname, employee_info in employee_dict.items():
    print(usrname)

    graph_title = "Hours for " + employee_info[0] + " " + employee_info[1]

    # running the def function display_graph for week/hours work pulling from the list on index 4/5
    display_graph(employee_info[4], employee_info[5], graph_title, graph_x_label, graph_y_label)
    print(employee_info[0] + " " + employee_info[1] + " was born in " + employee_info[2])

    # formating the table
    # looping 4 times to get each week and the hours for that week
    print("{:<8} {:<15}".format('Date','Hours'))
    for x in range(0,4):
        print("{:<8} {:<15}".format(employee_info[4][x],employee_info[5][x]))

    print("Average Hours " + str(employee_info[6][0]))
    print("The least hours worked was " + str(employee_info[6][1]))
    print("The most hours worked was " + str(employee_info[6][2]))

# EOF


