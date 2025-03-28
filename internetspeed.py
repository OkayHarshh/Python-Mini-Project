import tkinter as tk
from tkinter import ttk, messagebox
import speedtest
import threading
from tkinter import font as tkfont
from PIL import Image, ImageTk
import requests
from io import BytesIO
import random

class AestheticSpeedTest:
    def __init__(self, root):
        self.root = root
        self.root.title("✨ SpeedVibe")
        self.root.geometry("500x550")
        self.root.resizable(False, False)
        self.root.configure(bg="#fafafa")
        
        # Gen-Z aesthetic color palette
        self.colors = {
            "background": "#fafafa",
            "primary": "#6c5ce7",
            "secondary": "#a29bfe",
            "accent": "#fd79a8",
            "text": "#2d3436",
            "light_text": "#636e72",
            "success": "#00b894",
            "warning": "#fdcb6e",
            "error": "#e17055"
        }
        
        # Load aesthetic background image from URL
        try:
            response = requests.get("https://i.imgur.com/JKqJXWp.jpg")  # Pastel gradient image
            bg_image = Image.open(BytesIO(response.content))
            bg_image = bg_image.resize((500, 550), Image.Resampling.LANCZOS)
            self.bg_photo = ImageTk.PhotoImage(bg_image)
            self.background_label = tk.Label(root, image=self.bg_photo)
            self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        except:
            self.root.configure(bg=self.colors["background"])
        
        # Custom fonts
        self.title_font = tkfont.Font(family="Product Sans", size=22, weight="bold")
        self.button_font = tkfont.Font(family="Product Sans", size=12)
        self.result_font = tkfont.Font(family="Product Sans", size=14)
        self.status_font = tkfont.Font(family="Product Sans", size=10)
        
        # Style configuration
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        # Configure styles
        self.style.configure('TFrame', background=self.colors["background"])
        self.style.configure('TLabel', background=self.colors["background"], 
                           foreground=self.colors["text"], font=self.button_font)
        self.style.configure('TLabelframe', background="white", bordercolor="#e0e0e0", 
                            lightcolor="white", darkcolor="white", relief="flat")
        self.style.configure('TLabelframe.Label', background="white", 
                           foreground=self.colors["text"], font=self.button_font)
        self.style.configure('TButton', font=self.button_font, 
                            background=self.colors["primary"], foreground="white", 
                            borderwidth=0, focuscolor=self.colors["secondary"])
        self.style.map('TButton', 
                      background=[('active', self.colors["secondary"]), 
                                 ('disabled', '#b2bec3')],
                      foreground=[('disabled', '#dfe6e9')])
        
        # Custom progress bar style
        self.style.configure("Custom.Horizontal.TProgressbar", 
                           thickness=25, troughcolor="#e0e0e0", 
                           background=self.colors["accent"], lightcolor=self.colors["accent"], 
                           darkcolor=self.colors["accent"], bordercolor="#e0e0e0")
        
        # Main container
        self.main_frame = ttk.Frame(self.root, style='TFrame')
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=30, pady=30)
        
        # Header with aesthetic title
        self.header_frame = ttk.Frame(self.main_frame)
        self.header_frame.pack(fill=tk.X, pady=(0, 15))
        
        self.title_label = ttk.Label(
            self.header_frame, 
            text="✨ SpeedVibe", 
            font=self.title_font,
            foreground=self.colors["primary"]
        )
        self.title_label.pack(side=tk.LEFT)
        
        # Test button with emoji
        self.test_button = ttk.Button(
            self.main_frame, 
            text="🌐 Start Speed Test", 
            command=self.start_test_thread,
            style='TButton'
        )
        self.test_button.pack(pady=(10, 20), ipadx=30, ipady=10)
        
        # Progress bar with custom style
        self.progress = ttk.Progressbar(
            self.main_frame, 
            orient=tk.HORIZONTAL, 
            length=400, 
            mode='determinate',
            style="Custom.Horizontal.TProgressbar"
        )
        
        # Results frame with glassmorphism effect
        self.results_frame = ttk.LabelFrame(
            self.main_frame, 
            text=" Your Speed Vibe ",
            padding=(25, 15)
        )
        self.results_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        # Configure glassmorphism effect
        self.results_frame.configure(style='TLabelframe')
        
        # Result labels with emojis
        emoji_font = tkfont.Font(size=16)
        
        self.ping_label = ttk.Label(
            self.results_frame, 
            text="⏱ Ping: -- ms", 
            font=self.result_font
        )
        self.ping_label.pack(anchor=tk.W, pady=10)
        
        self.download_label = ttk.Label(
            self.results_frame, 
            text="💨 Download: -- Mbps", 
            font=self.result_font
        )
        self.download_label.pack(anchor=tk.W, pady=10)
        
        self.upload_label = ttk.Label(
            self.results_frame, 
            text="☁️ Upload: -- Mbps", 
            font=self.result_font
        )
        self.upload_label.pack(anchor=tk.W, pady=10)
        
        # Status label with random aesthetic messages
        self.status_messages = [
            "Ready to vibe check your internet ✨",
            "Let's measure those speedy vibes 🚀",
            "Your internet's main character moment 💫",
            "Speed test? More like vibe test 😎",
            "Loading... just kidding, we're fast ⚡"
        ]
        self.status_label = ttk.Label(
            self.main_frame, 
            text=random.choice(self.status_messages), 
            font=self.status_font,
            foreground=self.colors["light_text"]
        )
        self.status_label.pack(pady=(15, 5))
        
        # Footer with aesthetic touch
        self.footer_label = ttk.Label(
            self.main_frame, 
            text="made with 💜 • #aesthetic • v1.0", 
            font=self.status_font,
            foreground=self.colors["light_text"]
        )
        self.footer_label.pack(side=tk.BOTTOM, pady=(10, 0))
        
        # Animation variables
        self.animation_phrases = [
            "Checking those internet vibes",
            "Measuring your digital ✨aesthetic✨",
            "Speed test in progress",
            "Almost there, queen",
            "Slay, those bytes are moving"
        ]
        
    def start_test_thread(self):
        """Start the speed test in a separate thread"""
        self.test_button.config(state=tk.DISABLED)
        self.update_status(random.choice(self.animation_phrases))
        self.progress.pack(pady=10)
        self.progress['value'] = 0
        self.animate_progress()
        
        # Start the test in a separate thread
        threading.Thread(target=self.run_speed_test, daemon=True).start()
    
    def animate_progress(self):
        """Animate the progress bar smoothly"""
        if self.test_button['state'] == tk.DISABLED:
            current = self.progress['value']
            if current < 100:
                self.progress['value'] = current + 1.5
                self.root.after(20, self.animate_progress)
    
    def update_status(self, message):
        """Update status with random aesthetic dots"""
        dots = "." * (random.randint(1, 3))
        self.status_label.config(text=f"{message}{dots}")
    
    def run_speed_test(self):
        """Run the actual speed test"""
        try:
            st = speedtest.Speedtest()
            
            # Server selection
            self.root.after(0, lambda: self.update_status("Finding the vibeiest server"))
            st.get_best_server()
            
            # Download test
            self.root.after(0, lambda: self.update_status("Checking download slayage"))
            download_speed = st.download() / 1_000_000  # Convert to Mbps
            
            # Upload test
            self.root.after(0, lambda: self.update_status("Measuring upload flex"))
            upload_speed = st.upload() / 1_000_000  # Convert to Mbps
            
            # Get ping
            ping = st.results.ping
            
            # Update GUI with results
            self.root.after(0, lambda: self.update_results(ping, download_speed, upload_speed))
            self.root.after(0, lambda: self.progress.config(value=100))
            
        except Exception as e:
            self.root.after(0, lambda: messagebox.showerror(
                "Vibe Check Failed", 
                f"Couldn't measure your vibes: {str(e)}"
            ))
        finally:
            self.root.after(0, self.reset_ui)
    
    def update_results(self, ping, download, upload):
        """Update the result labels with aesthetic colors"""
        # Color coding based on speed
        ping_color = self.colors["success"] if ping < 50 else self.colors["warning"] if ping < 100 else self.colors["error"]
        download_color = self.colors["success"] if download > 50 else self.colors["warning"] if download > 20 else self.colors["error"]
        upload_color = self.colors["success"] if upload > 20 else self.colors["warning"] if upload > 5 else self.colors["error"]
        
        self.ping_label.config(
            text=f"⏱ Ping: {ping:.2f} ms", 
            foreground=ping_color
        )
        self.download_label.config(
            text=f"💨 Download: {download:.2f} Mbps", 
            foreground=download_color
        )
        self.upload_label.config(
            text=f"☁️ Upload: {upload:.2f} Mbps", 
            foreground=upload_color
        )
        
        # Generate a fun result message
        result_messages = [
            f"Your internet is {(download/100):.0%} vibe 🎉",
            "That's some main character internet right there ✨",
            "Internet slayage achieved 💅",
            "Speed demon alert! 🚗💨",
            "Those are some aesthetic bytes right there 🌈"
        ]
        self.status_label.config(
            text=random.choice(result_messages), 
            foreground=self.colors["primary"]
        )
    
    def reset_ui(self):
        """Reset the UI elements after test completion"""
        self.progress.pack_forget()
        self.test_button.config(state=tk.NORMAL)

def main():
    root = tk.Tk()
    
    # Set window icon (using emoji as fallback)
    try:
        root.iconbitmap('vibe.ico')  # Add your own aesthetic icon file
    except:
        pass
    
    # Center the window
    window_width = 500
    window_height = 550
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")
    
    app = AestheticSpeedTest(root)
    root.mainloop()

if __name__ == "__main__":
    main()