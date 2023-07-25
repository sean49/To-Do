def display_menu():
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Exit")

def add_task(tasks):
    task_name = input("Enter the task name: ")
    tasks[task_name] = False
    print(f"Task '{task_name}' added successfully!")

def view_tasks(tasks):
    print("Tasks:")
    for task, completed in tasks.items():
        status = "Completed" if completed else "Not Completed"
        print(f"- {task} ({status})")

def mark_task_completed(tasks):
    task_name = input("Enter the task name you want to mark as completed: ")
    if task_name in tasks:
        tasks[task_name] = True
        print(f"Task '{task_name}' marked as completed!")
    else:
        print(f"Task '{task_name}' not found!")

def main():
    tasks = {}
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_task_completed(tasks)
        elif choice == "4":
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
