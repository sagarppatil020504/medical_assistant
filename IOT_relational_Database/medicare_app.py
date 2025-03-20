import tkinter as tk
from tkinter import ttk, messagebox
import cv2
from PIL import Image, ImageTk
import queue
import patient_db
import connector_reco_db
import firebase_setup
import ttkbootstrap as tb
from ttkbootstrap import Style
from ttkbootstrap.widgets import Separator

# Initialize Firebase
firebase_setup.firebase().fire_main()

# Global Task Queue
task_queue = queue.Queue()

def process_tasks():
    while not task_queue.empty():
        task = task_queue.get()
        task()
    root.after(100, process_tasks)

class MedicalApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Medical Face Recognition System")
        self.root.geometry("900x650")
        self.style = Style(theme="superhero")
        
        self.running = False
        self.capture = None

        # Main container
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack(fill="both", expand=True)
        
        # Navigation Bar
        self.navbar = ttk.Frame(self.main_frame, width=200, padding=10, relief="ridge")
        self.navbar.pack(side="left", fill="y")
        
        ttk.Label(self.navbar, text="MENU", font=("Arial", 14, "bold"), anchor="center").pack(pady=10)
        Separator(self.navbar, bootstyle="info").pack(fill="x", pady=5)
        
        self.create_nav_buttons()
        
        # Content Frame
        self.content_frame = ttk.Frame(self.main_frame, padding=20)
        self.content_frame.pack(side="right", fill="both", expand=True)
        
        # Load Home Screen
        self.load_home_screen()

    def create_nav_buttons(self):
        ttk.Button(self.navbar, text="Home", bootstyle="primary-link", command=self.load_home_screen).pack(fill="x", pady=5)
        ttk.Button(self.navbar, text="Monitor Condition", bootstyle="primary-link", command=self.start_face_recognition).pack(fill="x", pady=5)
        ttk.Button(self.navbar, text="Patient Database", bootstyle="primary-link", command=self.manage_patients).pack(fill="x", pady=5)
        ttk.Button(self.navbar, text="Exit", bootstyle="danger-link", command=self.root.quit).pack(fill="x", pady=5)

    def load_home_screen(self):
        self.clear_content()
        ttk.Label(self.content_frame, text="Medical Face Recognition System", font=("Arial", 20, "bold")).pack(pady=20)
        ttk.Label(self.content_frame, text="Welcome! Select an option from the menu.", font=("Arial", 12)).pack()

    def clear_content(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()
    
    def start_face_recognition(self):
        self.clear_content()
        ttk.Label(self.content_frame, text="Face Recognition in Progress...", font=("Arial", 14, "bold")).pack(pady=10)
        
        self.video_frame = tk.Label(self.content_frame, borderwidth=3, relief="solid")
        self.video_frame.pack()

        self.running = True
        self.capture = cv2.VideoCapture(0)
        self.show_video()

    def show_video(self):
        if not self.running:
            return
        
        ret, frame = self.capture.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = cv2.resize(frame, (500, 350))
            img = ImageTk.PhotoImage(image=Image.fromarray(frame))
            self.video_frame.img = img
            self.video_frame.config(image=img)
        
        self.root.after(10, self.show_video)

    def manage_patients(self):
        self.clear_content()
        ttk.Label(self.content_frame, text="Patient Database Management", font=("Arial", 16, "bold")).pack(pady=10)
        
        frame = ttk.Frame(self.content_frame, padding=10)
        frame.pack()

        ttk.Button(frame, text="Add Patient", bootstyle="info", command=self.add_patient).pack(pady=5)
        ttk.Button(frame, text="Get Patients", bootstyle="info", command=self.get_patients).pack(pady=5)
        ttk.Button(frame, text="Update Patient", bootstyle="info", command=self.update_patient).pack(pady=5)
        ttk.Button(frame, text="Delete Patient", bootstyle="info", command=self.delete_patient).pack(pady=5)

    def add_patient(self):
        messagebox.showinfo("Feature", "Add Patient feature coming soon!")
    
    def get_patients(self):
        messagebox.showinfo("Feature", "Get Patients feature coming soon!")
    
    def update_patient(self):
        messagebox.showinfo("Feature", "Update Patient feature coming soon!")
    
    def delete_patient(self):
        messagebox.showinfo("Feature", "Delete Patient feature coming soon!")

if __name__ == "__main__":
    root = tb.Window(themename="superhero")
    app = MedicalApp(root)
    root.after(100, process_tasks)
    root.mainloop()
