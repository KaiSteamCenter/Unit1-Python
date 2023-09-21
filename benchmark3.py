"""
Task 1: Create a list
Create a list with 4 elements and print it.
"""

elements = ["gta", "minecraft", "ps5", "r6s"]
print(elements)
# Define a list of elements
# Print the elements

"""
Task 2: Add Element to a List
Add an element to the end of the list. Print the updated 
list.
"""

elements.append('payday3')
print(elements)
# Append 'payday3' to the list
# Print the updated list

"""
Task 3: Remove Element from a List
Remove a specific element from the list. Print the 
updated list.
"""

elements.remove('payday3')
print(elements)
# Remove 'payday3' from the list
# Print the updated list

"""
Task 4: Modify Element in a List
Modify an element at a specific index with a new value. 
Print the updated list.
"""

elements[3] = 'roblox' 
print(elements)
# Replace the element at index 3 with 'roblox'
# Print the updated list

"""
Task 5: Append Multiple Elements to a List
Append multiple elements to the end of the list. Print 
the updated list.
"""

elements.append('cod')
elements.append('mw2')
print(elements)
# Append 'cod' to the list
# Append 'mw2' to the list
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

