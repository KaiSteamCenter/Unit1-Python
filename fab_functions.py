# Task 1: Greeting Function
# Write a function `greet(name)` that takes a name as a parameter and prints a greeting message like "Hello, [name]!".

def greet(name): # Creates function w/ argument 'name'
    print("Hello", name) # Prints Hello w/ argument
greet("Mekhi") # Calls function w/ argument named 'Mekhi'



# Task 2: Sum of Two Numbers
# Write a function `sum_numbers(a, b)` that takes two numbers as parameters and returns their sum.

def sum_numbers(a, b): # Creates function w/ 2 arguments, a and b
    print(a + b) # Prints a + b, (Math Function)
sum_numbers(5,6) # Calls function w/ arguments 5 and 6

# Task 3: Calculate Factorial
# Write a function `factorial(n)` that calculates the factorial of a given number `n`.

def factorial(n): # Creates function w/ a argument 'n'
    if n <= 0: # Checks if n is equal to / less than 0, if it is it prints 1
        return 1
    else:
        return n * factorial(n - 1) # Else, does factorial (Math Function)
print(factorial(0)) # Prints factorial

# Task 4: Check Even or Odd
# Write a function `is_even(num)` that takes a number as a parameter and returns `True` if the number is even, and `False` otherwise.

def is_even(num): # Creates function w/ argument 'num'
    if num%2 == 0: # Checks if num has remainder of 0, being even. If 0, prints true, else, print false.
        print("True")
    else:
        print("False")

is_even(4) # Calls function w/ argument of 4

# Task 5: Calculate Area of a Rectangle
# Write a function `calculate_area(length, width)` that calculates and returns the area of a rectangle given its length and width.


def calculate_area(length, width): # Creates function w/ 2 arguments, 'length' and 'width'
    print(length * width) # Prints length * width (Math Function)

calculate_area(50, 50) # Calls function w/ argument of 50 and 50
