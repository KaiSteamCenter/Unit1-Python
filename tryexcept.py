while True:  # Makes infinite loop until 'break' is encountered.
    try:
        age = int(input('Enter your age: ')) # Asks user input for age (int)
        if age <= 21:
            print('You are not allowed to enter, you are too young.')
        else:
            print('Welcome, you are old enough.')
            break  # Breaks loop when age is valid
    except ValueError:
        print('Value Error')  

while True:  # Makes infinite loop until 'break' is encountered.
    try:
        faveNum = int(input('What is your favorite number: '))  # Asks user input for favorite number (int)
        break  # Breaks loop when faveNum is valid
    except ValueError:
        print('ValueError')  # Handles ValueError when faveNum is not int.


print("Fun Fact! Your age divided by your favorite number is:", age / faveNum) # Prints age / faveNum
