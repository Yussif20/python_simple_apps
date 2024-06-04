# List to store tasks
tasks = []

def add_task(task):
    """
    Add a task to the tasks list.
    
    Args:
        task (str): The task to add.
    """
    tasks.append(task)
    print("Task added.")

def remove_task(task):
    """
    Remove a task from the tasks list.
    
    Args:
        task (str): The task to remove.
    """
    if task in tasks:
        tasks.remove(task)
        print("Task removed.")
    else:
        print("Task not found.")

def view_tasks():
    """
    View all tasks in the tasks list.
    """
    if not tasks:
        print("No tasks to view.")
    else:
        for task in tasks:
            print(task)

def main():
    """
    Main function to run the todo list app.
    """
    while True:
        user_action = input("Please choose action (add, remove, view, or exit): ").strip().lower()
        if user_action == "add":
            task = input("Please add a task: ").strip()
            add_task(task)
        elif user_action == "remove":
            if not tasks:
                print("No tasks to remove.")
            else:
                task = input("Please choose a task to remove: ").strip()
                remove_task(task)
        elif user_action == "view":
            view_tasks()
        elif user_action == "exit":
            break
        else:
            print("Invalid action.")

# Run the main function to start the app
if __name__ == "__main__":
    main()
