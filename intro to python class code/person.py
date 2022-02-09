import datetime

# creating a class module called Person
class Person:

    """A model of a person"""

    def __init__(self, p_f_name, p_l_name, p_birth_yr):                 # argument assigned
        self.p_f_name = p_f_name
        self.p_l_name = p_l_name
        self.p_birth_yr = p_birth_yr

    def greetings(self):                                                # creating function called greetings
        greet = "Hello and Welcom, " + self.p_f_name + "."              # creating concat message with user first name

        return greet                                                    # return greet message

    def age(self):                                                      # creating function called age
        today = datetime.date.today()                                   # get today's date formated YYYY-MM-DD
        age = today.year - int(self.p_birth_yr)                         # taking today's date and only taking the YYYY and subtracting birth year of the person to get the age

        return age                                                      # return age
    
# EOF    
   



