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

# Input sentence
sentence = "This is a sample sentence with various words of different lengths"
# Split the sentence into words
words = sentence.split()
# Initialize an empty list to store the lengths
word_lengths = []
# Using a for loop to calculate and store the length of each word in the list
for word in words:
    word_lengths.append(len(word))
# Print the list of word lengths
print("Word lengths:", word_lengths)

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


for key, value in dict.items(): # iterates the dictionary and printing key-value

    print(f"{key}: {value}")