import datetime

# creating a class module called Person
class Person:

    """A model of a person"""

    def __init__(self, fname, lname, birthyr):                          # argument assigned
        self.fname = fname
        self.lname = lname
        self.birthyr = birthyr

    def greetings(self):                                                # creating function called greetings
        greet = "Hello and Welcom, " + self.fname + "."                 # creating concat message with user first name

        return greet                                                    # return greet message

    def age(self):                                                      # creating function called age
        today = datetime.date.today()                                   # get today's date formated YYYY-MM-DD
        age = today.year - int(self.birthyr)                            # taking today's date and only taking the YYYY and subtracting birth year of the person to get the age

        return age                                                      # return age
    
# EOF    
   
