def add_task(task_list):
    """Function to add a task to the list."""
    task = input("Enter a new task: ")
    task_list.append(task)
    print(f"Task added: {task}")

def view_tasks(task_list):
    """Function to display all tasks."""
    if not task_list:
        print("No tasks available.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(task_list, 1):
            print(f"{i}. {task}")

def remove_task(task_list):
    """Function to remove a task from the list."""
    view_tasks(task_list)
    if task_list:
        try:
            index = int(input("Enter the task number to remove: ")) - 1
            if 0 <= index < len(task_list):
                removed_task = task_list.pop(index)
                print(f"Removed task: {removed_task}")
            else:
                print("Invalid task number!")
        except ValueError:
            print("Please enter a valid number.")

def task_manager():
    """Main function to handle the task management app."""
    task_list = []
    print("Welcome to Task Management Application!")

    while True:
        print("\nOptions:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == "1":
            add_task(task_list)
        elif choice == "2":
            view_tasks(task_list)
        elif choice == "3":
            remove_task(task_list)
        elif choice == "4":
            print("Thank you for using Task Management Application. Goodbye!")
            break
        else:
            print("Invalid choice! Please select a valid option.")

# Run the Task Manager
task_manager()
