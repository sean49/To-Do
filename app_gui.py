import tkinter as tk
from tkinter import messagebox

def add_task():
    task_name = entry_task.get()
    if task_name:
        tasks[task_name] = False
        update_task_list()
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task name.")

def mark_task_completed():
    task_name = entry_task.get()
    if task_name in tasks:
        tasks[task_name] = True
        update_task_list()
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", f"Task '{task_name}' not found!")

def update_task_list():
    task_list.delete(0, tk.END)
    for task, completed in tasks.items():
        status = "Completed" if completed else "Not Completed"
        task_list.insert(tk.END, f"- {task} ({status})")

tasks = {}

root = tk.Tk()
root.title("To-Do List")

label_task = tk.Label(root, text="Enter task:")
label_task.pack()

entry_task = tk.Entry(root, width=30)
entry_task.pack()

button_add = tk.Button(root, text="Add Task", command=add_task)
button_add.pack()

button_mark_completed = tk.Button(root, text="Mark as Completed", command=mark_task_completed)
button_mark_completed.pack()

task_list = tk.Listbox(root, height=10, width=40)
task_list.pack()

root.mainloop()
