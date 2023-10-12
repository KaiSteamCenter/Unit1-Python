import datetime

"""
Exercise 1:
Write a Python program that prints the current date and time using the datetime module.
"""

print(datetime.datetime.now())

# Literal function??

"""
Exercise 2:
Write a Python program that prints the current date and time using the datetime module.
Using the strftime function format the date in standard U.S. date format (MM/DD/YYYY)
"""

x = datetime.datetime.now()

print(x.strftime("%m/%d/%Y"))   

# strftime returns the datetime.now as what I put it to be, being month / day / year.

"""
Exercise 3:
Using the strptime function, convert two strings into dates.
Then find the difference in days between the two.
"""

datestr = "09 09 2023"
datestr2 = "10 10 2023"

# Adds 2 variables of strings of dates.

date1 = datetime.datetime.strptime(datestr, "%m %d %Y")
date2 = datetime.datetime.strptime(datestr2, "%m %d %Y")

# Uses strptime to format the variables into a date, as month / day / year

difference = (date2 - date1).days

# Finds difference of date and time, by subtracting date2 by date1

print("The difference is", difference, "days")


"""
Excercise 4:
Write a program that asks the user for their birthdate and calculates their current 
age using the datetime module.
"""

birthdateStr = input("What is your birthday, MM/DD/YYYY: ")
# Input your birthday, form of M/D/Y


birthdate = datetime.datetime.strptime(birthdateStr,"%m/%d/%Y")
currentDate = datetime.datetime.now()

# Makes new variable named birthdate to transfer string input into birthdate input, being M/D/Y

age = currentDate.year - birthdate.year - ((currentDate.month, currentDate.day) < (birthdate.month, birthdate.day))

# Makes new variable to input age. (Subtracts current date from birth year), (Checks if current month and current day is less than birth month and day)

print("You are", age, "years old")




