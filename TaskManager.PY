# To-Do List Application in Python

def display_menu():
    """Display the menu options for the to-do list application."""
    print("\n----- To-Do List Menu -----")
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

def view_todo_list(todo_list):
    """Display the to-do list."""
    if len(todo_list) == 0:
        print("\nYour to-do list is empty.")
    else:
        print("\nYour To-Do List:")
        for index, task in enumerate(todo_list, start=1):
            status = "✓" if task['completed'] else "✗"
            print(f"{index}. {task['name']} [{status}]")

def add_task(todo_list):
    """Add a task to the to-do list."""
    task_name = input("Enter the task you want to add: ")
    todo_list.append({'name': task_name, 'completed': False})
    print(f"Task '{task_name}' added successfully!")

def mark_task_completed(todo_list):
    """Mark a task as completed."""
    if len(todo_list) == 0:
        print("Your to-do list is empty.")
        return

    view_todo_list(todo_list)
    try:
        task_num = int(input("Enter the number of the task you want to mark as completed: "))
        if 1 <= task_num <= len(todo_list):
            todo_list[task_num - 1]['completed'] = True
            print(f"Task '{todo_list[task_num - 1]['name']}' marked as completed!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input! Please enter a valid number.")

def delete_task(todo_list):
    """Delete a task from the to-do list."""
    if len(todo_list) == 0:
        print("Your to-do list is empty.")
        return

    view_todo_list(todo_list)
    try:
        task_num = int(input("Enter the number of the task you want to delete: "))
        if 1 <= task_num <= len(todo_list):
            removed_task = todo_list.pop(task_num - 1)
            print(f"Task '{removed_task['name']}' deleted successfully!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input! Please enter a valid number.")

def todo_list_app():
    """Main function to run the to-do list application."""
    todo_list = []
    while True:
        display_menu()
        try:
            choice = int(input("\nEnter your choice (1-5): "))
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            continue

        if choice == 1:
            view_todo_list(todo_list)
        elif choice == 2:
            add_task(todo_list)
        elif choice == 3:
            mark_task_completed(todo_list)
        elif choice == 4:
            delete_task(todo_list)
        elif choice == 5:
            print("Exiting the To-Do List application. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 5.")

# Run the To-Do List application
todo_list_app()
