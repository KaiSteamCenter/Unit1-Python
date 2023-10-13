"""
Task 1: Calculate the Square of a Number
Write a function that takes an integer as an argument and returns its square.
"""

def squareNum(a): # Creates function
    return a**2 # Returns value and does the power to the second.
print(squareNum(10)) # Calls function


"""
Task 2: Calculate the Area of a Rectangle:
Write a function that takes the length and width of a rectangle and returns its area.
"""

def rectArea(a, b): # Creates function
    return a * b # Returns value and multiples a by b
print(rectArea(5, 10)) # Calls function

"""
Task 3: Convert Temperature from Celsius to Fahrenheit:
Write a function that takes a temperature in Celsius and returns 
the equivalent temperature in Fahrenheit using the correct formula
"""

def temp(a): # Creates function
    return (a * (9/5)) + 32 # returns value, multiples a by (9/5), and adds 32
print(temp(1),"°C") # Calls function

"""
Task 4: Calculate the Average of Numbers:
Write a function that takes a list of numbers 
and returns the average (mean) of those numbers.
"""

def avgNumber(a): # Creates function
    total = sum(a) # Retrieves total of sum of list
    avg = total / len(a) # Retieves avg by dividing total by length of avg
    return avg # Returns avg value

print(avgNumber([6, 5, 4, 6, 2, 9, 15])) # Calls function