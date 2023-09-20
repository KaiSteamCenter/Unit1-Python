"""
TASK 1:
Create a float variable, and then convert it to an integer
Print both the original variable and the converted integer.

"""
fVariable = 1.1
vInt = int(fVariable)
print(fVariable)
print(vInt)
# Created a Float Var, then made another variable to make the float var into a int, printed both the float var and the int var.

"""
TASK 2:
    Write code that takes a number as input and prints whether 
it's positive, negative, or zero using if-elif-else statements.
"""
nmbr = int(input("what is the number?"))
if nmbr > 0:
    print("Number is Positive")
elif nmbr < 0:
    print("Number is Negative")
else:
    print("Number is Zero")
# Created a Int Input Var named nmbr, and made a if / elif / else statement where is nmbr is more than 0 its positive, less than 0 its negative, and anything else makes it nothing.
    
"""
TASK 3:
Write code that takes two numbers as input (an integer and a float), 
performs addition, subtraction, multiplication, and division, and prints the results.
"""
inte = int(input("Enter an integer: "))
float = float(input("Enter a float: "))

addition = inte + float
subtraction = inte - float
multiplication = inte * float

if float != 0:
    division = inte / float
else:
    division = "Not possible."

print(f"Addition: {inte} + {float} = {addition}")
print(f"Subtraction: {inte} - {float} = {subtraction}")
print(f"Multiplication: {inte} * {float} = {multiplication}")
print(f"Division: {inte} / {float} = {division}")
# made 2 vars for int and float, did all of the required PEMDAS, made it so division could be
# performed properly, and printed all 4 results (addition, subtraction, multiplication, division)


"""
TASK 4:
Create a dictionary with keys as fruit names and values as their respective quantities. 
Then print out the quantity of one of the fruits.
"""
fruit = {
    "apple":1,
    "banana":2,
    "cherry":3,
    "dewberry":4,
    "elderberry":5
    
}
fruit_name = input("Type the name of a Fruit Please: ")
if fruit_name in fruit:
    print(f"The quantity of {fruit_name} is {fruit[fruit_name]}.")
else:
    print(f"{fruit_name} is not in the fruit dictionary.")

# Made a dictionary with 5 fruits and 5 diffferent quantities.
# Made the user input a random fruit name
# Made a if statement whereif the fruit is in the dictionary, it tells how many items there are,
# and if its not in the dictionary it tells them the fruit isn't in the dictionary


"""
TASK 5:

Create a string variable with that is a list of numbers and convert that string into a tuple.
Then print out the both the original string and tuple.
"""

nmbrs = "1, 2, 3, 4, 5"

nmbrsList = nmbrs.split(', ')
nmbrsTuple = tuple(int(num) for num in nmbrsList)
print('Original String = ', nmbrs)
print('List = ', nmbrsList)
print('Tuple = ', nmbrsTuple)

# created a string var called nmbrs
# made a list by splitting the nmbrs string
# made into a tuple by making the numbers in the nmbrsList into a int
# printed the original sstring and the tuple.