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




"""
4. Password Guessing Game:
Create a simple password guessing game using a while loop. Ask the user to guess a predefined password and provide appropriate feedback.
"""

password = "password123"

# Initialize the number of attempts
attempts = 5

while attempts > 0:
    # Ask the user for their guess
    guess = input("Enter your password guess: ")

    # Check if the guess is correct
    if guess == password:
        print("You guessed the correct password.")
        break
    else:
        attempts -= 1
        if attempts > 0:
            print(f"Wrong password. You have {attempts} {'attempts' if attempts > 1 else 'attempt'} left.")
        else:
            print("Game over!")

"""
5. Sum of Digits:
Write a program that calculates the sum of the digits of a given number using a while loop.
"""

while i < 15:
    n1 = float(input("Input a 1st number: "))
    n2 = float(input("Input a 2nd number: "))


"""
6. Fibonacci Series:
Write a program that prints the first n numbers in the Fibonacci sequence using a while loop.
"""