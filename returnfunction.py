"""
Task 1: Calculate the Square of a Number
Write a function that takes an integer as an argument and returns its square.
"""

def squareNum(a): # Creates function
    return a**2 # Returns value and does the power to the second.
print(squareNum(10)) # Calls function

assert squareNum(7) == 49
try:
    assert squareNum(5) == 25
except:
    print("Assert is wrong.")

# Assert the result of calling 'squareNum' with the argument: 7
# Assert the result of calling 'squareNum' with the argument: 5
# If the assertion in the 'try/except' block fails, print "Assert is wrong."


"""
Task 2: Calculate the Area of a Rectangle:
Write a function that takes the length and width of a rectangle and returns its area.
"""

def rectArea(a, b): # Creates function
    return a * b # Returns value and multiples a by b
print(rectArea(5, 10)) # Calls function

assert rectArea(10,10) == 100
try:
    assert rectArea(2.5, 5) == 12.5
except:
    print("Assert is wrong.")

# Assert the result of calling 'rectArea' with the 2 arguments: 10 , 10
# Assert the result of calling 'rectArea' with the 2 arguments: 2.5, 5
# If the assertion in the 'try/except' block fails, print "Assert is wrong."

"""
Task 3: Convert Temperature from Celsius to Fahrenheit:
Write a function that takes a temperature in Celsius and returns 
the equivalent temperature in Fahrenheit using the correct formula
"""

def temp(a): # Creates function
    return (a * (9/5)) + 32 # returns value, multiples a by (9/5), and adds 32
print(temp(1),"°C") # Calls function

assert temp(5) == 41
try:
    assert temp(18) == 64.4
except:
    print("Assert is wrong.")

# Assert the result of calling 'temp' with the argument: 5
# Assert the result of calling 'avgNumber' with the argument: 18
# If the assertion in the 'try/except' block fails, print "Assert is wrong."
"""
Task 4: Calculate the Average of Numbers:
Write a function that takes a list of numbers 
and returns the average (mean) of those numbers.
"""

def avgNumber(a): # Creates function
    total = sum(a) # Retrieves total of sum of list
    return total / len(a) # Returns and retieves avg by dividing total by length of avg

print(avgNumber([6, 5, 4, 6, 2, 9, 15])) # Calls function

assert avgNumber([6, 4, 32, 5, 4, 2, 3]) == 8 
try:
    assert avgNumber([5,10,15]) == 10
except:
    print("Assert is wrong.")
# Assert the result of calling 'avgNumber' with the first list
# Assert the result of calling 'avgNumber' with the second list
# If the assertion in the 'try/except' block fails, print "Assert is wrong."
