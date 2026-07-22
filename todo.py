import json
import os
from datetime import datetime
from colorama import Fore, Style, init

init(autoreset=True)

FILE = "tasks.json"


def load_tasks():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r") as f:
        return json.load(f)


def save_tasks(tasks):
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=4)


def add_task(tasks):
    title = input("Task: ")
    due = input("Due Date (YYYY-MM-DD): ")

    tasks.append({
        "title": title,
        "due": due,
        "completed": False
    })

    save_tasks(tasks)
    print("Task Added.")


def view_tasks(tasks, status="all"):
    if not tasks:
        print("No tasks.")
        return

    today = datetime.today().date()

    for i, task in enumerate(tasks, start=1):

        if status == "pending" and task["completed"]:
            continue

        if status == "completed" and not task["completed"]:
            continue

        due_date = datetime.strptime(task["due"], "%Y-%m-%d").date()

        overdue = ""

        if not task["completed"] and due_date < today:
            overdue = Fore.RED + " (OVERDUE)"

        if task["completed"]:
            color = Fore.GREEN
            state = "Completed"
        else:
            color = Fore.YELLOW
            state = "Pending"

        print(color + f"{i}. {task['title']} | {state} | Due: {task['due']}{overdue}")


def update_task(tasks):
    view_tasks(tasks)

    if not tasks:
        return

    n = int(input("Task number: ")) - 1

    tasks[n]["title"] = input("New title: ")
    tasks[n]["due"] = input("New due date (YYYY-MM-DD): ")

    save_tasks(tasks)
    print("Updated.")


def delete_task(tasks):
    view_tasks(tasks)

    if not tasks:
        return

    n = int(input("Task number: ")) - 1

    tasks.pop(n)

    save_tasks(tasks)
    print("Deleted.")


def complete_task(tasks):
    view_tasks(tasks)

    if not tasks:
        return

    n = int(input("Task number: ")) - 1

    tasks[n]["completed"] = True

    save_tasks(tasks)
    print("Marked Completed.")


while True:
    tasks = load_tasks()

    print("\n===== TO-DO APP =====")
    print("1. Add Task")
    print("2. View All")
    print("3. View Pending")
    print("4. View Completed")
    print("5. Update Task")
    print("6. Delete Task")
    print("7. Mark Complete")
    print("8. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_task(tasks)

    elif choice == "2":
        view_tasks(tasks)

    elif choice == "3":
        view_tasks(tasks, "pending")

    elif choice == "4":
        view_tasks(tasks, "completed")

    elif choice == "5":
        update_task(tasks)

    elif choice == "6":
        delete_task(tasks)

    elif choice == "7":
        complete_task(tasks)

    elif choice == "8":
        break

    else:
        print("Invalid choice.")