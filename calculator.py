"""
Using your knowledge of conditionals and math operations in python. Create a two number calculator.

Your calculator should ask the user for two numbers, and then perform a math operation using those two numbers. Your code must support decimal values.

The operations your calculator should support are the following:

Addition
Subtraction
Multiplication
Division
Exponents
Floor Division
Remainder
    
Tell the user if they put a letter instead of a number
If the user chooses division and the denominator is 0 tell them that you cannot calculate with that number
"""
# Imports math because why not?
import math

# Made a function for each of the 7 Operations.

def addition(num1, num2):
    return num1 + num2
def subtract(num1, num2):
    return num1 - num2
def multiply(num1, num2):
    return num1 * num2
def division(num1, num2):
    if num2 == 0:
        return "Division by zero returns as infinite."
    # If number is 0 its not becomes inf
    return num1 / num2
def exponent(num1, num2):
    return num1 ** num2
def floordivision(num1, num2):
    if num2 == 0:
        return "Division by zero returns as infinite."
    # If number is 0 its not becomes inf
    return num1 // num2
def remainder(num1, num2):
    if num2 == 0:
        return "Division by zero returns as infinite"
    # If number is 0 its not becomes inf
    return num1 % num2

# Made a function for each of the 7 Operations.


# Has the user input 2 different numbers.
# Uses a try/except block to make sure that the user uses a float.

while True:
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        break  # Exit the loop if both inputs are valid floats
    except ValueError:
        print("Invalid input. Please enter numeric values.")


# Has the user input which operation they want to use.

operation = input("Which Operation do you want, Addition, Subtraction, Multiplication, Division, Exponents, Floor Division, Remainder. (1-7): ")

# Make a If statement saying that if user input (operation) is equal to 1-7, it does whichever operation it is.

if operation == '1':
    print("Result:", addition(num1, num2))
elif operation == '2':
    print("Result:", subtract(num1, num2))
elif operation == '3':
    print("Result:", multiply(num1, num2))
elif operation == '4':
    print("Result:", division(num1, num2))
elif operation == '5':
    print("Result:", exponent(num1, num2))
elif operation == '6':
    print("Result:", floordivision(num1, num2))
elif operation == '7':
    print("Result:", remainder(num1, num2))
else:
    print("Invalid choice")