#Import Section

from datetime import date   #import this for Date
import getpass              #import this for User
import json                 #import json to use json files
import matplotlib.pyplot as plt     #import matplot to use graph
import csv                          #import csv to use csv files
import requests                     #import to request calls to an API
import warnings
from urllib3.exceptions import  InsecureRequestWarning
warnings.simplefilter('ignore',InsecureRequestWarning)
import ssl

#Flower Box Section

#########################################################
#                                                       
#   Name:  Thai Vo                        
#   Date:  03/11/2022
#   Program Description:
#
#   using pyplot to create graphs to plot the weeks and 
#   hours worked for min and max housr for each employees
#   Using googles API to pull information for a book
#                                                       
#########################################################

#Variables section

    #All variables needed for will be declared here

graph_title = ""
graph_x_label = "Week Ending"
graph_y_label = "Hours Worked"
hours_worked = 'hours_worked.csv'
api_addr = "https://www.googleapis.com/books/v1/volumes"
worked_dates_list = []
max_hrs_list = []
min_hrs_list = []
employee_names = []

#Functions section

def display_graph(employees, max_hrs, min_hrs, graph_title, graph_x_label, graph_y_label):
    """function to configuring and displaying a graph in a range for min and max values"""
    plt.style.use('seaborn-dark')
    fig, ax = plt.subplots()
    ax.plot(employees, max_hrs, c='purple')
    ax.plot(employees, min_hrs, c='blue')
    ax.fill_between(employees, max_hrs, min_hrs, facecolor='green', alpha=0.2)
    # Set chart title and label axes.
    ax.set_title(graph_title, fontsize=20)
    ax.set_xlabel(graph_x_label, fontsize=10)
    ax.set_ylabel(graph_y_label, fontsize=10)
    # Set size of tick labels.
    ax.tick_params(axis="both", labelsize=10)
    plt.show(block=True)    
    
def csv_get():
    """Importing a CSV file so that it can be read and has an exception error"""
    try:
        with open(hours_worked, 'r') as f:
            reader = csv.reader(open(hours_worked, 'r'))
            return reader
    except FileNotFoundError:
        print(f"File: {f} not found.")

def book_info(query):
    """Generating information about a book from Google's API"""
    key = "AIzaSyDCqGGoZVAH83KX-QqCqoRxIdvT8fNssKs"                     # API key
    api_addr = "https://www.googleapis.com/books/v1/volumes"            # URL to google's book API volume
    params = {"q": query, "maxResults": 1, "key": key}                  # params to add to the end of the url to pull the information 
    responses = requests.get(api_addr, params=params)                   # calling a request
    response = responses.json()                                         # request in the form of a json file
    
    # looping to the json file to get all the information for the book and return the results
    for book in response["items"]:                                      
        volume = book["volumeInfo"]
        title = volume["title"]
        industryIDs = volume["industryIdentifiers"]
        ISBN_info = industryIDs[0]
        ISBN_number = ISBN_info["identifier"]
        ISBN_type = ISBN_info["type"]
        authors = volume["authors"]
        author = authors[0].replace("()","")
        isbn = ISBN_type + ": " + ISBN_number

        return title, author, isbn

#Input section

# reading in the employees data txt file data as a dictionary into a json file
# added exception handling if the file isn't founded
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

print("Enter a book title to get details on the book.")
query = input("What is your favorite book? ")


#Process section
    #All processing of user input and calculations will be in this section
    #Make sure to use line comments to fully explain how the data is being processed

# call for the csv_get function 
# and loop through the top row but remove the first cell in A1 as it is not a date
# all the dates then get added to the list
reader = csv_get()
header = next(reader)
for day in header:
    if "weeks" not in day:
        worked_dates_list.append(day)

# the title of the graph that ply will generate
graph_title = "Employee Min and Max hours worked for " + worked_dates_list[0] + " to " + worked_dates_list[-1]

# looping through each employee and getting their hours worked
for usrname in employee_dict.keys():
    hrs_worked_list = []
    hrs_worked_list_converted = []
    reader = csv_get()

    # null the first entry as it is the username and not a set of hours
    # looping get each hours and add to the list
    for hrs in reader:
        if hrs[0] == usrname:
            hrs_worked_list = list(hrs)
            hrs_worked_list.pop(0)
            i = 0
            while i < len(hrs_worked_list):
                hrs_worked_list_converted.append(int(hrs_worked_list[i]))
                i = i + 1
            # calcuate avg, min, max values
            if len(hrs_worked_list):
                avg_hrs = sum(hrs_worked_list_converted) / len(hrs_worked_list_converted)
                min_hrs = min(hrs_worked_list_converted)
                max_hrs = max(hrs_worked_list_converted)
                worked_hrs_stat = [avg_hrs, min_hrs, max_hrs]
                employee_dict[usrname].append(worked_dates_list)
                employee_dict[usrname].append(hrs_worked_list_converted)
                employee_dict[usrname].append(worked_hrs_stat)

# looping each username and employee to get their work values to add to a list for max, min
for usrname, employee_info in employee_dict.items():
    employee_name = employee_info[0] + " " + employee_info[1][0]
    worked_min = employee_info[6][1]
    worked_max = employee_info[6][2] 
    employee_names.append(employee_name)       
    max_hrs_list.append(worked_max)
    min_hrs_list.append(worked_min)

# get the information for the book the user input to get the values
title, author, isbn = book_info(query)

#Output section

    #Your Username and Today's Date will be in this section and ALWAYS First
    #All output in the form of print functions will be in this section
    #Make sure to use line comments to fully explain what is being displayed and how it is formatted

print(getpass.getuser())                # output username
print(date.today())                     # output today's date

# create graph for each employee and create a table of the week and hours worked.
for usrname, employee_info in employee_dict.items():
    print(usrname)

    print(employee_info[0] + " " + employee_info[1] + " was born in " + employee_info[2])

    # formating the table
    # looping 4 times to get each week and the hours for that week
    print("{:<8} {:<15}".format('Date','Hours'))
    for i in range(0,len(employee_info[4])):
        print("{:<8} {:<15}".format(employee_info[4][i],employee_info[5][i]))

    print("Average Hours " + str(employee_info[6][0]))
    print("The least hours worked was " + str(employee_info[6][1]))
    print("The most hours worked was " + str(employee_info[6][2]))

display_graph(employee_names, min_hrs_list, max_hrs_list, graph_title, graph_x_label, graph_y_label)

print(employee_dict)
print(f"{title} by {author} | {isbn}")
# EOF


