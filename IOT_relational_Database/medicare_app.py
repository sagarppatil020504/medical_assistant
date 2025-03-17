import tkinter as tk
from tkinter import ttk, messagebox, Canvas, Scrollbar
import cv2
from PIL import Image, ImageTk
import queue
import patient_db
import connector_reco_db
import firebase_setup
import ttkbootstrap as tb  # Importing ttkbootstrap for modern themes

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
        self.root.geometry("850x650")
        self.root.configure(bg='#f4f4f4')  # Light gray background

        self.video_frame = None
        self.capture = None
        self.running = False

        # Apply Theme
        self.style = tb.Style(theme="superhero")  # Themes: cosmo, flatly, superhero, etc.

        self.create_main_menu()

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def create_main_menu(self):
        self.clear_screen()
        frame = ttk.Frame(self.root, padding=20)
        frame.pack(pady=30)

        ttk.Label(frame, text="Medical Face Recognition System", font=("Arial", 20, "bold")).pack(pady=20)

        btn_style = {"width": 30, "padding": 10}  # Common Button Styling

        ttk.Button(frame, text="Monitor Condition (Face Recognition)", style="primary.Outline.TButton", command=self.start_face_recognition).pack(pady=10)
        ttk.Button(frame, text="Staff Work (Patient Database Operations)", style="primary.Outline.TButton", command=self.manage_patients).pack(pady=10)
        ttk.Button(frame, text="Exit", style="danger.TButton", command=self.root.quit).pack(pady=10)

    def start_face_recognition(self):
        self.clear_screen()
        ttk.Label(self.root, text="Face Recognition in Progress...", font=("Arial", 14, "bold")).pack(pady=10)

        frame = ttk.Frame(self.root, padding=10)
        frame.pack(pady=10)

        self.video_frame = tk.Label(frame, borderwidth=3, relief="solid")
        self.video_frame.pack()

        ttk.Button(self.root, text="Back", style="secondary.TButton", command=self.create_main_menu).pack(pady=10)

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
        self.clear_screen()
        ttk.Label(self.root, text="Patient Database Management", font=("Arial", 16, "bold")).pack(pady=10)

        frame = ttk.Frame(self.root, padding=10)
        frame.pack()

        ttk.Button(frame, text="Add Patient", style="info.TButton", command=self.add_patient).pack(pady=5)
        ttk.Button(frame, text="Get Patients", style="info.TButton", command=self.get_patients).pack(pady=5)
        ttk.Button(frame, text="Update Patient", style="info.TButton", command=self.update_patient).pack(pady=5)
        ttk.Button(frame, text="Delete Patient", style="info.TButton", command=self.delete_patient).pack(pady=5)
        ttk.Button(frame, text="Back", style="secondary.TButton", command=self.create_main_menu).pack(pady=10)

    def add_patient(self):
        self.clear_screen()
        ttk.Label(self.root, text="Add New Patient", font=("Arial", 14, "bold")).pack(pady=10)

        frame = ttk.Frame(self.root, padding=10)
        frame.pack()

        ttk.Label(frame, text="Name:").pack(anchor="w")
        name_entry = ttk.Entry(frame)
        name_entry.pack(pady=5, fill="x")

        ttk.Label(frame, text="Age:").pack(anchor="w")
        age_entry = ttk.Entry(frame)
        age_entry.pack(pady=5, fill="x")

        ttk.Label(frame, text="Condition:").pack(anchor="w")
        condition_entry = ttk.Entry(frame)
        condition_entry.pack(pady=5, fill="x")

        def submit():
            name = name_entry.get().strip()
            age = age_entry.get().strip()
            condition = condition_entry.get().strip()
            if name and age and condition:
                P_id = name[:3] + "123"
                patient_db.MedicalRecords().add_patient(P_id, name, age, condition, [], [], False, "")
                messagebox.showinfo("Success", "Patient added successfully!")
                self.manage_patients()
            else:
                messagebox.showerror("Error", "All fields are required!")

        ttk.Button(frame, text="Submit", style="success.TButton", command=submit).pack(pady=10)
        ttk.Button(frame, text="Back", style="secondary.TButton", command=self.manage_patients).pack()

    def get_patients(self):
        self.clear_screen()
        ttk.Label(self.root, text="Patient List", font=("Arial", 14, "bold")).pack(pady=10)

        # Scrollable Patient List
        canvas = Canvas(self.root)
        scroll_y = Scrollbar(self.root, orient="vertical", command=canvas.yview)

        frame = ttk.Frame(canvas)
        canvas.create_window((0, 0), window=frame, anchor="nw")

        patients = patient_db.MedicalRecords().get_all_patients()
        if patients:
            for p in patients:
                ttk.Label(frame, text=f"{p['P_id']} - {p['pat_name']} ({p['medical_cond']})", padding=5).pack(anchor="w")
        else:
            ttk.Label(frame, text="No patients found.", padding=5).pack()

        frame.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"), yscrollcommand=scroll_y.set)

        canvas.pack(fill="both", expand=True, side="left")
        scroll_y.pack(fill="y", side="right")

        ttk.Button(self.root, text="Back", style="secondary.TButton", command=self.manage_patients).pack(pady=10)

    def update_patient(self):
        messagebox.showinfo("Feature", "Update patient feature coming soon!")

    def delete_patient(self):
        messagebox.showinfo("Feature", "Delete patient feature coming soon!")

if __name__ == "__main__":
    root = tb.Window(themename="superhero")  # Using ttkbootstrap Window
    app = MedicalApp(root)
    root.after(100, process_tasks)
    root.mainloop()
