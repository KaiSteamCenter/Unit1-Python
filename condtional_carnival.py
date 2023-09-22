'''
TASK 1 Even or Odd
Determine if a number is even or odd.
'''
num = int(input("Enter a number: "))

if num % 2 == 0:
    print(str(num) + "is just a even number.")
else:
    print(str(num) + " is an odd number.")

# Prompt the user to enter a number and store it in the 'num' variable
# Check if the entered number is even
# If number is not even, it prints that the number is odd.

'''
TASK 2 Positive, Negative, or Zero:
Determine if a number is positive, negative, or zero.

EXTRA CREDIT: Tell the user if they did not enter a valid number
'''

user_input = input("Enter a number: ")
try:
    number = float(user_input)
except ValueError:
    print("Invalid input. Please enter a valid number.")
else:
    if number > 0:
        print("The number is positive.")
    elif number < 0:
        print("The number is negative.")
    else:
        print("The number is zero.")

# Prompt the user to enter a number and store it in the 'user_input' variable
# Try to convert the user's input to a floating-point number
# If the input is not a valid number, handle the ValueError exception
# Check if the number is greater than zero
# Check if the number is less than zero
# If neither condition above is met, the number must be zero

'''
TASK 3: Largest of Three
Find and print the largest of three numbers.
'''

n1 = float(input("first number: "))
n2 = float(input("second number: "))
n3 = float(input("third number: "))

largest = max(n1, n2, n3)
print("The largest number is:", largest)

# Prompt the user to enter 3 'float' numbers and input it into their specific variables
# Makes a new variable to get the max number out of those 3 variables
# Prints the largest number aka the "largest" variable


'''
TASK 4: Leap Year
Determine if a year is a leap year or not.
'''

year = int(input("Enter a year: "))
if year%4==0:
    print("The year is a leap year.")
else:
    print("The year isn't a leap year.")

# Prompt the user to enter a year and store it in the 'year' variable
# Check if the entered year is divisible by 4, being a leap year
# Prints if the input is a leap year, or isn't.

'''
TASK 5: Vowel or Consonant:
Identify if a character is a vowel or consonant.

EXTRA CREDIT: Tell the user if they did not enter a valid letter
'''

input_user = input("Pick a Singular Character: ")
vowels = ('a','e','i','o','u')
input_user = input_user.lower()

if input_user == vowels:
    print("That is a vowel")
else:
    print("That is a consonant.")
    
if not input_user.isalpha() or len(input_user) != 1:
    print("You did not enter a valid letter.")
    
# Prompt the user to enter a singular character and store it in the 'input_user' variable
# Define a tuple of vowels
# Makes user's input lowercase automatically
# If the user input is a,e,i,o,u, then it is printed as a vowel, and if not it is a consonant.
# Check if the user's input is not a valid letter
# If it's not valid, it prints that it's not a valid letter.

