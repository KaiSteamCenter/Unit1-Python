"""
Task 1: Create a list
Create a list with 4 elements and print it.
"""

elements = ["element1", "element2", "element3", "element4"]
print(elements)
# Define a list of elements
# Print the elements

"""
Task 2: Add Element to a List
Add an element to the end of the list. Print the updated 
list.
"""

elements.append('element5')
print(elements)
# Append 'element5' to the list
# Print the updated list

"""
Task 3: Remove Element from a List
Remove a specific element from the list. Print the 
updated list.
"""

elements.remove('element5')
print(elements)
# Remove 'element5' from the list
# Print the updated list

"""
Task 4: Modify Element in a List
Modify an element at a specific index with a new value. 
Print the updated list.
"""

elements[3] = 'element_rewritten' 
print(elements)
# Replace the element at index 3 with 'element_rewritten'
# Print the updated list

"""
Task 5: Append Multiple Elements to a List
Append multiple elements to the end of the list. Print 
the updated list.
"""

elements.append('element4')
elements.append('element5')
print(elements)
# Append 'element4' to the list
# Append 'element5' to the list
# Print the updated list

"""
Task 6: Delete Element at a Specific Index
Delete an element at a specific index. Print the updated 
list.
"""

del elements[5]
print(elements)
# Delete the element at index 5
# Print the updated list

"""
Task 7: Subsetting lists
Create a new variable equal to the first 2 items of your list
Then print out the new variable
"""

elementsExtended = (elements[0:2])
print(elementsExtended)
# Create a new list 'elementsExtended' containing elements from index 0 to 1 (inclusive) of the 'elements' list
# Print the 'elementsExtended' list

"""
Task 8: Extend a List
Extend the list with the elements of another list. Print 
the updated list.
"""

elements.extend(elementsExtended)
print(elements)
# Extend the 'elements' list by adding the contents of 'elementsExtended'
# Print the updated 'elements' list

