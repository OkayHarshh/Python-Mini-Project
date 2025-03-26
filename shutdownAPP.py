from tkinter import *
import os

# Create the main window
root = Tk()
root.title("Shutdown APP")
root.geometry("300x200")
root.config(bg="black")

# Shutdown Button
shutdown_button = Button(root, text="Shutdown", command=lambda: os.system("shutdown /s /t 5"), bg="red", fg="white")
shutdown_button.pack(pady=10)

# Restart Button
restart_button = Button(root, text="Restart", command=lambda: os.system("shutdown /r /t 5"), bg="green", fg="white")
restart_button.pack(pady=10)

# Log Off Button
logoff_button = Button(root, text="Log Off", command=lambda: os.system("shutdown /l"), bg="blue", fg="white")
logoff_button.pack(pady=10)

# Run the main loop
root.mainloop()
