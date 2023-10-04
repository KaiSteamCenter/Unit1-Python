todos = []
#empty list, used to store todos.

def display_todos():
    print("\nYour current todos are:\n")
    if not todos:
        print("No todos yet!")
    else:
        for i, todo in enumerate(todos, start=1):
            print(f"{i}. {todo}")
            


while True:
    display_todos()
    
    useraction = input("Would you like to add or remove a todo? (add/remove) ").lower()
    if useraction == "add":
        new_todo = input("What is your new todo? ")
        todos.append(new_todo)
    elif useraction == "remove":
        try:
            # Ask the user which todo to remove by its index
            index_to_remove = int(input("Which # todo would you like to remove: ")) - 1
            if 0 <= index_to_remove < len(todos):
                removed_todo = todos.pop(index_to_remove)
                print(f"Removed: {removed_todo}")
            else:
                print("Invalid index. Please enter a valid index.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    elif useraction == "quit":
        print("Goodbye!")
        break
    else:
        print("Invalid input. Please enter 'add', 'remove', or 'quit'.")