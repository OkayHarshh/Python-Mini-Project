import tkinter as tk
from tkinter import messagebox

# Function to add a task
def add_task():
    task = task_entry.get().strip()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

# Function to remove a selected task
def remove_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to remove.")

# Function to clear all tasks
def clear_tasks():
    task_listbox.delete(0, tk.END)

# Function to exit the application
def exit_app():
    root.destroy()

# Creating the main window
root = tk.Tk()
root.title("Task Management App")
root.geometry("400x500")
root.configure(bg="#f0f0f0")

# Title Label
title_label = tk.Label(root, text="Task Management", font=("Arial", 16, "bold"), bg="#f0f0f0")
title_label.pack(pady=10)

# Task Entry Box
task_entry = tk.Entry(root, font=("Arial", 12), width=30)
task_entry.pack(pady=5)

# Add Task Button
add_button = tk.Button(root, text="Add Task", font=("Arial", 12), bg="#4CAF50", fg="white", command=add_task)
add_button.pack(pady=5)

# Task Listbox
task_listbox = tk.Listbox(root, font=("Arial", 12), width=40, height=10)
task_listbox.pack(pady=10)

# Buttons for Task Actions
remove_button = tk.Button(root, text="Remove Task", font=("Arial", 12), bg="#FF5733", fg="white", command=remove_task)
remove_button.pack(pady=5)

clear_button = tk.Button(root, text="Clear All Tasks", font=("Arial", 12), bg="#FF9800", fg="white", command=clear_tasks)
clear_button.pack(pady=5)

exit_button = tk.Button(root, text="Exit", font=("Arial", 12), bg="#607D8B", fg="white", command=exit_app)
exit_button.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()

