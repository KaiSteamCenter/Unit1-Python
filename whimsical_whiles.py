"""
1. Simple Counter:
Write a program that uses a while loop to print numbers from 1 to 10.
"""

i = 1
while i <= 10:
    print(i)
    i += 1

# Makes a var named i
# Makes a while i is less than or equal to 10
# While the I condition is true, prints i and adds 1 after printing.

"""
2. Countdown:
Write a program that uses a while loop to print numbers from 10 to 1 in descending order.
"""

i = 10
while i >= 1:
    print(i)
    i -= 1

# Makes a var named i
# Makes a while i is greater than than or equal to 0
# While the I condition is true, prints i and subtracts 1 after printing.

"""
3. Factorial Calculation:
Write a program that calculates the factorial of a given number using a while loop.
"""

num = int(input("Enter a number: "))

factor = 1

if num < 0:
    print("Error")
elif num == 0:
    print("The factorial of 0 is 1.")
else:
    while num > 0:
        factor *= num
        num -= 1
    
    print(f"The factorial is: {factor}")

# Input from the user
# Initialize the factorial to 1
# Check if the number is negative, zero, or positive
# Calculate the factorial using a while loop
# Prints factorial


"""
4. Password Guessing Game:
Create a simple password guessing game using a while loop. Ask the user to guess a predefined password and provide appropriate feedback.
"""

password = "password123"

# Initialize the number of attempts
attempts = 5

while attempts > 0:
    guess = input("Enter your password guess: ")
    if guess == password:
        print("You guessed the correct password.")
        break
    else:
        attempts -= 1
        if attempts > 0:
            print(f"Wrong password. You have {attempts} {'attempts' if attempts > 1 else 'attempt'} left.")
        else:
            print("Game over!")
    # Ask the user for their guess
    # Check if the guess is correct
    # Subtracts attempts by 1.
    # changes from attempts to attempt once it says "1"


"""
5. Sum of Digits:
Write a program that calculates the sum of the digits of a given number using a while loop.
"""
totsum = 0

for i in range(5):
    num = int(input("Enter a number: "))
    
    original_num = num
    sum_of_digits = 0
    
    while num > 0:
        digit = num % 10 
        sum_of_digits += digit
        num //= 10  
    
    totsum += sum_of_digits


# makes a variable to store the total sum of digits
# Loop five times (for five different numbers)
# Input from the user, asking for a number
# Calculate the sum of digits for the current number using a while loop
# Get the last digit ("ex: 123 --> 3")
# adds digit to the sum.
# Removes last digit ("ex: 123 --> 12")


print(f"The total sum of the digits for all five numbers is: {totsum}")


"""
6. Fibonacci Series:
Write a program that prints the first n numbers in the Fibonacci sequence using a while loop.
"""

n = int(input("Enter the number of Fibonacci numbers to generate: "))

a, b = 0, 1
for i in range(n):
    print(a)
    a, b = b, a + b

# Take user input for the number of Fibonacci numbers.
# Initialize variables to represent the first two numbers
# Use a loop to generate and print the first 'n' Fibonacci numbers
# Calculate the next number and update 'a' and 'b'
