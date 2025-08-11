import sqlite3
from datetime import datetime

# Connect to DB
conn = sqlite3.connect('todo.db')
c = conn.cursor()

# Create table
c.execute('''CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    description TEXT,
    due_date TEXT,
    status TEXT DEFAULT 'pending')''')

conn.commit()

# Function to add task
def add_task():
    title = input("Enter task title: ")
    description = input("Enter description: ")
    due_date = input("Enter due date (YYYY-MM-DD): ")
    c.execute("INSERT INTO tasks (title, description, due_date) VALUES (?, ?, ?)", (title, description, due_date))
    conn.commit()
    print("Task added!")

# Function to show all tasks
def view_tasks():
    c.execute("SELECT * FROM tasks")
    for row in c.fetchall():
        print(row)

# Function to mark task complete
def complete_task(task_id):
    c.execute("UPDATE tasks SET status='done' WHERE id=?", (task_id,))
    conn.commit()

# Function to delete a task
def delete_task(task_id):
    c.execute("DELETE FROM tasks WHERE id=?", (task_id,))
    conn.commit()

# Menu
while True:
    print("\n1. Add Task\n2. View Tasks\n3. Complete Task\n4. Delete Task\n5. Exit")
    choice = input("Choose: ")
    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        complete_task(int(input("Enter task ID: ")))
    elif choice == '4':
        delete_task(int(input("Enter task ID: ")))
    elif choice == '5':
        break