import tkinter as tk
from tkinter import filedialog , messagebox

def newfile():
    text.delete(1.0, tk.END)

def openfile():
    filepath = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
    if filepath:
        with open(filepath, "r") as file:
            text.delete(1.0, tk.END)
            text.insert(1.0, file.read())

def savefile():
    filepath = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
    if filepath:
        with open(filepath, "w") as file:
            file.write(text.get(1.0, tk.END))   
            messagebox.showinfo("File Saved", "File has been saved successfully")         

root = tk.Tk()
root.title("File Editor")
root.geometry("800x600")

menu = tk.Menu(root)
root.config(menu=menu)

file_menu = tk.Menu(menu, tearoff=False)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=newfile)
file_menu.add_command(label="Open", command=openfile)
file_menu.add_command(label="Save", command=savefile)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

text = tk.Text(root, wrap=tk.WORD,font = ("Times New Roman", 18), fg = "black", bg = "white")
text.pack(expand=True, fill=tk.BOTH)

root.mainloop()