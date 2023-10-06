todos = []
# Created an empty list to store todos.

def display_todos():
    # Define a function to display todos.
    print("\nYour current todos are:\n")
    if not todos:
        print("No todos yet!")
    else:
        for i, todo in enumerate(todos, start=1):
            # Enumerate through the todos and display them with their index.

            print(f"{i}. {todo}")

         

# Main loop to interact with the user.
while True:
    # Call the display_todos function to show the current list of todos.
    display_todos()
    
    # Ask the user what action they want to perform (add/remove/stop).
    useraction = input("Would you like to add or remove a todo? (add/remove/stop) ").lower()
    
    # Check if the user wants to add a todo.
    if useraction == "add":
        # Prompt the user to enter a new todo and append it to the todos list.
        new_todo = input("What is your new todo? ")
        todos.append(new_todo)
        
    # Check if the user wants to remove a todo.
    elif useraction == "remove" or useraction == "del" or useraction == "delete":
        try:
            # Ask the user which todo to remove by its index.
            index_to_remove = int(input("Which # todo would you like to remove: ")) - 1
            if 0 <= index_to_remove < len(todos):
                # Remove the todo at the specified index and display a confirmation message.
                removed_todo = todos[index_to_remove]  # Store the item to be removed
                del todos[index_to_remove]  # Delete the item from the list               
                print(f"Removed: {removed_todo}")
            else:
                # Handle the case of an invalid index.
                print("Invalid index. Please enter a valid index.")
                
        except ValueError:
            # Handle the case of invalid input (non-integer).
            print("Invalid input. Please enter a valid number.")
            
  # Check if the user wants to stop the program.
    elif useraction == "stop":
        # Display a goodbye message and exit the loop to end the program.
        print("Goodbye!")
        break
    
    # Handle invalid user input.
    else:
        print("Invalid input. Please enter 'add', 'remove', or 'quit'.")