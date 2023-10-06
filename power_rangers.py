"""
Exercise 1:
Write a program to print numbers from 1 to 10 using a for loop.
"""

for i in range(1, 11): # Iterates from 1 to 10.
    print(i)

"""
Exercise 2:
Write a program to count by 10s from 900 to 1000
"""

for i in range(900, 1001, 10): # Iterates from 900 to 1000 with a increment of 10
    print(i)

"""
Exercise 3:
Write a program that counts form 1-100 by 9
"""

for i in range(1, 101, 9): # Iterates from 1 to 100 with a increment of 9
    print(i)

print("hello")
"""
Exercise 4:
Write a program to calculate the sum of all numbers from 1 to 10 using a for loop.
"""

sum = 0 # Defines a variable to print at the end (sum)
for i in range(1, 11): # Range starting at 1, ending at 10
    sum += i # Adds i (number) to the sum
print(sum)

"""
Excercise 5:
Uncomment the following code and run it. Then answer the following:
- What is the ouput of the code?

- Explain the iterative process that this code executes to get that output
"""

rows = 5
 
for i in range(rows):
    for j in range(i + 1):
        print('*', end=' ')
    print()
    
""" 
Output of code: 
*
* *
* * *
* * * *
* * * * *
"""
# First 'for loop' line says for i (0 - 4) in the range of rows (5)
    # Every iteration essentially says that each row will print a asterisk, and add a space to the end so it won't print multiple lines
    # First lines go from 1 to 2 and soforth because of the second 'for loop', where the range is added i + 1, and stops before the 5th row.
    