'''
Exercise 1:
Check if an integer is even and greater than 10.
Return True if both conditions are met, False otherwise.
'''

def intfunc(number):
    return number % 2 == 0 and number > 10 
# Defines a function named 'intfunc' that takes a single argument 'number'
# Check if 'number' is both even and greater than 10


number = int(input("Give me a number (int): "))
print(intfunc(number)) 
# Asks the user to give a integer-based number
# Prints the 'intfunc' function.

'''
Exercise 2:
Determine the ticket price based on age and student status.
Price is $10 if under 18 or a student, $20 otherwise.
'''

age = int(input("What is your age: "))
student = input("Are you a student (yes/no): ")
# Asks the user to input their age as a int
# Asks the user to input if their a student with the specific words 'yes' or 'no'
if age < 18 or student == 'yes':
    print("Price is $10")
else:
    print("Price is $20")
# Checks if user's age is less than 18 or a student, if it is then price is 10 dollars
# if neither is true then it would be printed that the price is 20

'''
Exercise 3:
Prompt the user to enter a fruit name. Check if the fruit is in the list. 
If it is, print "Yes, that fruit is in the list." 
If it's not, print "No, that fruit is not in the list."
'''

fruits = ["apple", "banana", "cherry", "pomegranate", "grape", "orange", "kiwi"]
# Created a list of fruits

fruitCheck = input("Please type a random fruit name: ")
# Asks the user to input a random fruit name
if fruitCheck in fruits:
    print("Yes, that fruit is in the list.")
else:
    print("No, that fruit is not in the list.")
# Checks if the inputted variable is inside the list of 'fruits'
# If it is, Yes
# If it isn't, No

'''
Exercise 4:
Check if a year is a century year and a leap year.
'''

year = int(input("Enter a year: "))

centuryyear = year % 100 == 0

leapyear = (year % 4 == 0)
# Check if it's a century year (divided by 100)
# Check if it's a leap year (divided by 4)

if centuryyear:
    print(f"{year} is a century year.")
else:
    print(f"{year} is not a century year.")

if leapyear:
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
# Display the result

'''
Exercise 5:
Calculate the cost of shipping for an online order based on the order weight and destination zone. 
The shipping cost is $5 per kilogram for Zone A and $7 per kilogram for Zone B. 
If the order weight is less than 0 kg, return an error message.
'''

zoneA = 5
zoneB = 7
orderWeight = float(input("Input the Order Weight: "))
destZone = input("Enter the Destination Zone: ")

# Asks the user to input their order weight in a foat, and the destination zone to be A or B.

if orderWeight <= 0:
    print("Error: Order Weight must be more than 0 kilograms.")
else:
    if destZone == "A":
        shipping_cost = orderWeight * zoneA
        print(f"Shipping cost to Zone A: ${shipping_cost:.2f}")
    elif destZone == "B":
        shipping_cost = orderWeight * zoneB
        print(f"Shipping cost to Zone B: ${shipping_cost:.2f}")
    else:
        print("Error: Please enter 'A' or 'B'.")
# Checks if order weight is less than 0, inputs error
# Checks if destZone is A or B, and multiplies and tells shipping cost
# If anything else happens, print error.

'''
Exercise 6:
Determine the type of a triangle based on side lengths.
Equilateral, Isosceles, Scalene, or Not a triangle.
'''

side1 = float(input("first side: "))
side2 = float(input("second side: "))
side3 = float(input("third side: "))
# Ask the user to enter the lengths of the three sides of the triangle

if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1: # Check if the input forms a valid triangle 
    if side1 == side2 == side3:
        print("It's an Equilateral triangle.")
    elif side1 == side2 or side1 == side3 or side2 == side3:
        print("It's an Isosceles triangle.")
    else:
        print("It's a Scalene triangle.")
else:
    print("Error: It's not a triangle.")
    # Check for the type of triangle
