from itertools import cycle
import tkinter as tk
from PIL import Image, ImageTk
import os

# Initialize the main window
root = tk.Tk()
root.title("Image Slideshow")
root.attributes("-fullscreen", True)  # Make the window fullscreen
root.configure(bg="black")  # Set background color to black

# List of Image paths (replace with your actual image paths)
imagePaths = [
    r"C:\Users\RP Mandal\Pictures\Screenshots\Screenshot (606).png",
    r"C:\Users\RP Mandal\Pictures\Screenshots\Screenshot (607).png",
    r"C:\Users\RP Mandal\Pictures\Screenshots\Screenshot (610).png"
]

# Verify paths
for path in imagePaths:
    if not os.path.exists(path):
        print(f"Error: File not found - {path}")
    else:
        print(f"Found file: {path}")

# Resize the images to fit the screen
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
imagesize = (screen_width, screen_height)

# Create a cycle iterator for the image paths
image_paths_cycle = cycle(imagePaths)

# Label to display the images
label = tk.Label(root, bg="black")
label.pack(expand=True, fill="both")

# Function to update the slideshow
def update_slideshow():
    # Get the next image path from the cycle
    image_path = next(image_paths_cycle)
    
    try:
        # Open and resize the image
        img = Image.open(image_path)
         # Resize the image
        photo = ImageTk.PhotoImage(img)
        
        # Update the label with the new image
        label.config(image=photo)
        label.image = photo  # Keep a reference to avoid garbage collection
    except Exception as e:
        print(f"Error loading image: {e}")
    
    # Schedule the next update after 5 seconds
    root.after(2000, update_slideshow)

# Function to exit the application
def exit_app():
    root.destroy()

# Add an exit button
exit_button = tk.Button(
    root,
    text="Exit",
    font=("Arial", 16),
    bg="red",
    fg="white",
    bd=0,  # No border
    command=exit_app
)
exit_button.place(relx=0.98, rely=0.02, anchor="ne")  # Position in the top-right corner

# Start the slideshow
update_slideshow()

# Run the Tkinter main loop
root.mainloop()
