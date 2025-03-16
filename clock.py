import tkinter as tk
from time import strftime
import random

root = tk.Tk()
root.title("Digital Clock")
root.geometry("300x150")
root.eval('tk::PlaceWindow . center')  # Center window

def time():
    string = strftime('%H:%M:%S %p \n %D')
    label.config(text=string)
    label.after(1000, time)


label = tk.Label(root, font=('calibri', 40, 'bold'), background='black', foreground='white')
label.pack(anchor='center')

exit_button = tk.Button(root, text="Exit", command=root.destroy, font=("calibri", 12, "bold"))
exit_button.pack(pady=10)

time()

root.mainloop()


