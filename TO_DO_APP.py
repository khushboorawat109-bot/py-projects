import tkinter as tk
from tkinter import messagebox
import json
import os

# File to store tasks
FILE_NAME = "tasks.json"

# Load tasks from file
def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

# Save tasks to file
def save_tasks():
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file)

# Add task
def add_task():
    task = entry.get()
    if task == "":
        messagebox.showwarning("Warning", "Enter a task")
    else:
        tasks.append({"task": task, "done": False})
        entry.delete(0, tk.END)
        update_listbox()
        save_tasks()

# Delete task
def delete_task():
    try:
        selected = listbox.curselection()[0]
        tasks.pop(selected)
        update_listbox()
        save_tasks()
    except:
        messagebox.showwarning("Warning", "Select a task")

# Mark task as done
def mark_done():
    try:
        selected = listbox.curselection()[0]
        tasks[selected]["done"] = True
        update_listbox()
        save_tasks()
    except:
        messagebox.showwarning("Warning", "Select a task")

# Update listbox display
def update_listbox():
    listbox.delete(0, tk.END)
    for task in tasks:
        if task["done"]:
            listbox.insert(tk.END, "✔ " + task["task"])
        else:
            listbox.insert(tk.END, task["task"])

# Main window
root = tk.Tk()
root.title("To-Do App")
root.geometry("400x450")

tasks = load_tasks()

# Input field
entry = tk.Entry(root, width=30, font=("Arial", 14))
entry.pack(pady=10)

# Buttons
add_btn = tk.Button(root, text="Add Task", width=15, command=add_task)
add_btn.pack(pady=5)

done_btn = tk.Button(root, text="Mark as Done", width=15, command=mark_done)
done_btn.pack(pady=5)

delete_btn = tk.Button(root, text="Delete Task", width=15, command=delete_task)
delete_btn.pack(pady=5)

# Listbox
listbox = tk.Listbox(root, width=40, height=15, font=("Arial", 12))
listbox.pack(pady=10)

update_listbox()

root.mainloop()