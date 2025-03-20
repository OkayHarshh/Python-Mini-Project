import tkinter as tk
from tkinter import messagebox, scrolledtext

# Initialize the main window
root = tk.Tk()
root.title("Contact Book App")
root.geometry("500x400")  # Set window size

# Dictionary to store contacts
contacts = {}

# Function to create a new contact
def create_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()

    if name and phone and email:
        if name in contacts:
            messagebox.showwarning("Duplicate", "Contact already exists.")
        else:
            contacts[name] = {"phone": phone, "email": email}
            messagebox.showinfo("Success", "Contact added successfully.")
            clear_entries()
    else:
        messagebox.showwarning("Input Error", "Please fill all fields.")

# Function to view all contacts
def view_contacts():
    if not contacts:
        messagebox.showinfo("No Contacts", "No contacts found.")
    else:
        contact_list = ""
        for name, contact in contacts.items():
            contact_list += f"{name}: Phone: {contact['phone']}, Email: {contact['email']}\n"
        view_window = tk.Toplevel(root)
        view_window.title("All Contacts")
        text_area = scrolledtext.ScrolledText(view_window, width=50, height=20)
        text_area.insert(tk.INSERT, contact_list)
        text_area.pack()

# Function to update a contact
def update_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()

    if name in contacts:
        contacts[name] = {"phone": phone, "email": email}
        messagebox.showinfo("Success", "Contact updated successfully.")
        clear_entries()
    else:
        messagebox.showwarning("Not Found", "Contact not found.")

# Function to delete a contact
def delete_contact():
    name = name_entry.get()
    if name in contacts:
        del contacts[name]
        messagebox.showinfo("Success", "Contact deleted successfully.")
        clear_entries()
    else:
        messagebox.showwarning("Not Found", "Contact not found.")

# Function to search for a contact
def search_contact():
    name = name_entry.get()
    if name in contacts:
        contact = contacts[name]
        messagebox.showinfo("Contact Found", f"{name}: Phone: {contact['phone']}, Email: {contact['email']}")
    else:
        messagebox.showwarning("Not Found", "Contact not found.")

# Function to clear entry fields
def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)

# GUI Layout
# Labels
tk.Label(root, text="Name:").grid(row=0, column=0, padx=10, pady=10)
tk.Label(root, text="Phone:").grid(row=1, column=0, padx=10, pady=10)
tk.Label(root, text="Email:").grid(row=2, column=0, padx=10, pady=10)

# Entry fields
name_entry = tk.Entry(root, width=30)
name_entry.grid(row=0, column=1, padx=10, pady=10)
phone_entry = tk.Entry(root, width=30)
phone_entry.grid(row=1, column=1, padx=10, pady=10)
email_entry = tk.Entry(root, width=30)
email_entry.grid(row=2, column=1, padx=10, pady=10)

# Buttons
tk.Button(root, text="Create Contact", command=create_contact).grid(row=3, column=0, padx=10, pady=10)
tk.Button(root, text="View Contacts", command=view_contacts).grid(row=3, column=1, padx=10, pady=10)
tk.Button(root, text="Update Contact", command=update_contact).grid(row=4, column=0, padx=10, pady=10)
tk.Button(root, text="Delete Contact", command=delete_contact).grid(row=4, column=1, padx=10, pady=10)
tk.Button(root, text="Search Contact", command=search_contact).grid(row=5, column=0, padx=10, pady=10)
tk.Button(root, text="Exit", command=root.quit).grid(row=5, column=1, padx=10, pady=10)

# Run the application
root.mainloop()