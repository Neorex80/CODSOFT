import datetime
import json
import os
from colorama import init, Fore, Style

init(autoreset=True)  # Initialize colorama

class TodoList:
    def __init__(self, filename):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                return json.load(file)
        else:
            return []

    def save_tasks(self):
        with open(self.filename, 'w') as file:
            json.dump(self.tasks, file, indent=4)

    def add_task(self):
        print(Fore.CYAN + "===== Add a New Task =====" + Style.RESET_ALL)
        task_name = input("Enter the task name: ")
        task_description = input("Enter the task description: ")
        task_due_date = input("Enter the task due date (YYYY-MM-DD): ")
        task_priority = input("Enter the task priority (High, Medium, Low): ")

        task = {
            "name": task_name,
            "description": task_description,
            "due_date": task_due_date,
            "priority": task_priority,
            "done": False,
            "created_at": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        self.tasks.append(task)
        self.save_tasks()
        print(Fore.GREEN + "Task added!" + Style.RESET_ALL)

    def view_tasks(self):
        print("\n" + Fore.CYAN + "===== Tasks =====" + Style.RESET_ALL)
        if not self.tasks:
            print(Fore.RED + "No tasks available." + Style.RESET_ALL)
        for index, task in enumerate(self.tasks):
            status = Fore.GREEN + "Done" + Style.RESET_ALL if task["done"] else Fore.RED + "Not Done" + Style.RESET_ALL
            print(f"{index + 1}. {task['name']} - {status}")
            print(f"  Description: {task['description']}")
            print(f"  Due Date: {task['due_date']}")
            print(f"  Priority: {task['priority']}")
            print(f"  Created At: {task['created_at']}\n")

    def mark_task_as_done(self):
        print(Fore.CYAN + "===== Mark Task as Done =====" + Style.RESET_ALL)
        task_index = int(input("Enter the task number to mark as done: ")) - 1
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]["done"] = True
            self.save_tasks()
            print(Fore.GREEN + "Task marked as done!" + Style.RESET_ALL)
        else:
            print(Fore.RED + "Invalid task number." + Style.RESET_ALL)

    def delete_task(self):
        print(Fore.CYAN + "===== Delete a Task =====" + Style.RESET_ALL)
        task_index = int(input("Enter the task number to delete: ")) - 1
        if 0 <= task_index < len(self.tasks):
            del self.tasks[task_index]
            self.save_tasks()
            print(Fore.GREEN + "Task deleted!" + Style.RESET_ALL)
        else:
            print(Fore.RED + "Invalid task number." + Style.RESET_ALL)

    def search_tasks(self):
        print(Fore.CYAN + "===== Search Tasks =====" + Style.RESET_ALL)
        search_term = input("Enter the search term: ")
        found_tasks = [task for task in self.tasks if search_term.lower() in task["name"].lower() or search_term.lower() in task["description"].lower()]
        if found_tasks:
            print("\n" + Fore.CYAN + "Found Tasks:" + Style.RESET_ALL)
            for index, task in enumerate(found_tasks):
                status = Fore.GREEN + "Done" + Style.RESET_ALL if task["done"] else Fore.RED + "Not Done" + Style.RESET_ALL
                print(f"{index + 1}. {task['name']} - {status}")
                print(f"  Description: {task['description']}")
                print(f"  Due Date: {task['due_date']}")
                print(f"  Priority: {task['priority']}")
                print(f"  Created At: {task['created_at']}\n")
        else:
            print(Fore.RED + "No tasks found." + Style.RESET_ALL)

def main():
    todo_list = TodoList("tasks.json")

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen
        todo_list.view_tasks()
        print("\n" + Fore.CYAN + "===== To-Do List Menu =====" + Style.RESET_ALL)
        print(Fore.CYAN + "1. Add Task" + Style.RESET_ALL)
        print(Fore.CYAN + "2. Mark Task as Done" + Style.RESET_ALL)
        print(Fore.CYAN + "3. Delete Task" + Style.RESET_ALL)
        print(Fore.CYAN + "4. Search Tasks" + Style.RESET_ALL)
        print(Fore.CYAN + "5. Exit" + Style.RESET_ALL)

        choice = input("Enter your choice: ")

        if choice == '1':
            todo_list.add_task()
        elif choice == '2':
            todo_list.mark_task_as_done()
        elif choice == '3':
            todo_list.delete_task()
        elif choice == '4':
            todo_list.search_tasks()
        elif choice == '5':
            print(Fore.GREEN + "Exiting the To-Do List." + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + "Invalid choice. Please try again." + Style.RESET_ALL)
        input(Fore.YELLOW + "Press Enter to continue..." + Style.RESET_ALL)

if __name__ == "__main__":
    main()
