"""
Exercise 1:
Write a program to print each character of a given string using a for loop.
"""

inputtedString = input("Write something that consists of a string: ") # user inputs a string or anything.
for char in inputtedString: #for however many characters in user inputted string, it separates each char and prints.
    print(char)

"""
Exercise 2:
Write a program to calculate the sum of elements in a list using a for loop.
"""

numlist = [50, 20, 30] # inputs num list
sum = 0 # initilizes a var to store the su
for num in numlist:
    sum += num # uses a loop to add sum from numlist
print("The sum is:", sum) #prints the sum

"""
Exercise 3:
Write a program to print the length of each word in a sentence using a for loop and a list.
"""

sentence = "this is a sample sentenence that make no sense"
words = sentence.split()

for x in words:
    print(f"The length of", {x}, "is", len(x))

"""
Excercise 4:
Write a program that creates a dictionary (atleast 4 key:value pairs) and then
iterates through a dictionary and prints the result

In a comment, answer the following, what do you notice about the output of your code?
Is it what you expected?
"""



dict = {
    'name': "Mekhi",
    'age': "17",
    'residence': "brooklyn",
    'job': "student"
} # Create a dict with at least four key-value pairs


for x in dict: # iterates the dictionary and printing the key of 
    print(x)
    # I notice that once printed, the code shows the 4 keys in different lines of code. This is not what I expected. 
    # I had expected for us to be printing both the key and the value.