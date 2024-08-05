# To-Do List Application

This is a simple command-line To-Do List application written in Python. It allows users to manage their tasks efficiently with features like adding tasks, marking tasks as done, deleting tasks, and searching tasks. The tasks are saved in a JSON file for persistence.

## Features

- **Add Task**: Add a new task with a name, description, due date, and priority.
- **View Tasks**: View all tasks along with their details and status.
- **Mark Task as Done**: Mark a specified task as completed.
- **Delete Task**: Delete a specified task from the list.
- **Search Tasks**: Search tasks by name or description.

## Prerequisites

- Python 3.x
- `colorama` library for colored terminal output

You can install the `colorama` library using pip:

```bash
pip install colorama
```

## Usage

1. Clone the repository or download the `todo_list.py` file.

2. Open your terminal and navigate to the directory containing `todo_list.py`.

3. Run the application:

```bash
python todo_list.py
```

## How to Use

### Main Menu

When you run the application, you will see the main menu with the following options:

```
===== To-Do List Menu =====
1. Add Task
2. Mark Task as Done
3. Delete Task
4. Search Tasks
5. Exit
```

### Adding a Task

1. Choose option `1` from the main menu.
2. Enter the task details when prompted:
   - Task Name
   - Task Description
   - Task Due Date (in YYYY-MM-DD format)
   - Task Priority (High, Medium, Low)
3. The task will be added to the list and saved to `tasks.json`.

### Viewing Tasks

The tasks are automatically displayed on the screen whenever you interact with the menu. Each task shows its name, description, due date, priority, creation date, and completion status.

### Marking a Task as Done

1. Choose option `2` from the main menu.
2. Enter the task number to mark as done.
3. The task status will be updated to "Done".

### Deleting a Task

1. Choose option `3` from the main menu.
2. Enter the task number to delete.
3. The task will be removed from the list and `tasks.json` will be updated.

### Searching Tasks

1. Choose option `4` from the main menu.
2. Enter the search term.
3. The application will display tasks that match the search term in their name or description.

### Exiting the Application

Choose option `5` from the main menu to exit the application.

## Example

```
===== Tasks =====
1. Complete Python project - Not Done
  Description: Finish the coding and testing of the Python project.
  Due Date: 2024-08-15
  Priority: High
  Created At: 2024-08-05 10:20:30

===== To-Do List Menu =====
1. Add Task
2. Mark Task as Done
3. Delete Task
4. Search Tasks
5. Exit
Enter your choice: 1
===== Add a New Task =====
Enter the task name: Buy groceries
Enter the task description: Buy milk, eggs, and bread.
Enter the task due date (YYYY-MM-DD): 2024-08-06
Enter the task priority (High, Medium, Low): Medium
Task added!

Press Enter to continue...
```

## License

This project is licensed under the MIT License.

## Acknowledgements

This application was developed with the help of the `colorama` library for colorful terminal output.

---
