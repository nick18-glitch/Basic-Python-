tasks = []

def add_task():
    task = input("Enter new task: ")
    tasks.append({"task": task, "done": False})

def view_tasks():
    print("\nYour Checklist:\n")
    for idx, t in enumerate(tasks, start=1):
        status = "✓" if t["done"] else " "
        print(f"{idx}. [{status}] {t['task']}")
    print()

def mark_done():
    view_tasks()
    try:
        num = int(input("Enter task number to mark as done: "))
        if 1 <= num <= len(tasks):
            tasks[num - 1]["done"] = True
            print("Task marked as done.\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid number.\n")

def delete_task():
    view_tasks()
    try:
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            deleted = tasks.pop(num - 1)
            print(f"Deleted: {deleted['task']}\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid number.\n")

def menu():
    while True:
        print("=== Checklist Menu ===")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            mark_done()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Exiting... Bye!")
            break
        else:
            print("Invalid choice. Try again.\n")

menu()







