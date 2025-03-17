import firebase_admin
from firebase_admin import credentials, db
from worker_db import task_queue  # Assuming task_queue is defined in worker_db
from photo_comparator import PhotoComparator
import time
import datetime
import queue

# ✅ Prevent multiple initializations
if not firebase_admin._apps:
    cred = credentials.Certificate("vishwas-patra-firebase-adminsdk-lbb9f-e67ac71793.json")
    firebase_admin.initialize_app(cred, {
        "databaseURL": "https://vishwas-patra-default-rtdb.asia-southeast1.firebasedatabase.app/",
        "storageBucket": "vishwas-patra.appspot.com"
    })

class MedicalRecords:
    def __init__(self):
        self.ref = db.reference('/patients')  # Firebase Path
        self.add_task = queue.Queue()  # Initialize a separate queue if needed

    # 🔹 CREATE (Add Patient Record) without photo URL in the record
    def add_patient(self, P_id, pat_name, age, medical_cond, Medicines, time_medicines, Medicine_taken, photo_path):
        def task():
            print(f"🆔 Patient ID: {P_id}, Photo Path: {photo_path}")
            # Use PhotoComparator to process the photo (e.g., capture or verify photo exists)
            # The photo comparator will handle capturing/updating the local photo for the patient,
            # but we will not store its URL in the patient record.
            pc = PhotoComparator()
            pc.process_photo(P_id)  # Process the photo in the local folder

            patient_ref = self.ref.child(P_id)
            if patient_ref.get() is None:  # Ensure unique P_id
                # Create patient record without the "photo" field
                patient_ref.set({
                    "P_id": P_id,
                    "pat_name": pat_name,
                    "age": age,
                    "medical_cond": medical_cond,
                    "Medicines": Medicines,
                    "time_medicines": time_medicines,
                    "Medicine_taken": Medicine_taken,
                })
                print(f"✅ Patient '{pat_name}' added successfully!")
            else:
                print("⚠️ Error: Patient ID must be unique!")
        task_queue.put(task)

    # 🔹 READ (Fetch Patient Records)
    def get_patients(self):
        def task():
            patients = self.ref.get()
            if patients:
                print("\n📋 List of Patients:")
                for key, data in patients.items():
                    print(f"🆔 {data['P_id']} | Name: {data['pat_name']} | Condition: {data['medical_cond']}")
            else:
                print("⚠️ No patients found!")
        task_queue.put(task)
        
    def get_patients_withPid(self, P_id):
        def task():
            patients = self.ref.get()
            if patients:
                for key, data in patients.items():
                    if data.get('P_id') == P_id:
                        print("\n📋 Patient Details:")
                        print(f"🆔 Patient ID: {data['P_id']}")
                        print(f"👤 Name: {data['pat_name']}")
                        print(f"🔢 Age: {data.get('age', 'N/A')}")
                        print(f"🩺 Condition: {data['medical_cond']}")
                        print(f"💊 Medicines: {', '.join(data.get('Medicines', []))}")
                        print(f"⏰ Medicine Time: {', '.join(data.get('time_medicines', []))}")
                        print(f"✅ Medicine Taken: {'Yes' if data.get('Medicine_taken', False) else 'No'}")
                        return
                print("⚠️ No patient found with the given ID.")
            else:
                print("⚠️ No patients available in the database!")
        task_queue.put(task)

    # 🔹 UPDATE (Modify Patient Data)
    def update_patient(self, P_id, updated_data):
        def task():
            patient_ref = self.ref.child(P_id)
            if patient_ref.get():
                patient_ref.update(updated_data)
                print(f"✅ Patient '{P_id}' updated successfully!")
            else:
                print("⚠️ Error: Patient ID not found!")
        task_queue.put(task)

    # 🔹 DELETE (Remove a Patient Record)
    def delete_patient(self, P_id):
        def task():
            patient_ref = self.ref.child(P_id)
            if patient_ref.get():
                patient_ref.delete()
                print(f"✅ Patient '{P_id}' deleted successfully!")
            else:
                print("⚠️ Error: Patient ID not found!")
        task_queue.put(task)

# ------------------------ Example Usage ------------------------

# if __name__ == "__main__":
#     # Assume task_queue is processed by worker_db.db_worker() in a separate thread.
#     # This connector code simply adds tasks to the queue.
#     records = MedicalRecords()

#     # Example: Adding a new patient
#     pat_name = input("👤 Enter patient name: ").strip()
#     add_photo = input("📷 Would you like to add a patient photo? (y/n): ").strip().lower()
#     photo_path = ""

#     # Generate a unique patient ID using first 3 letters of name and timestamp.
#     secrete_pid = datetime.datetime.now()
#     P_id = pat_name[:3] + secrete_pid.strftime("%Y%m%d%H%M%S")
#     print(f"🆔 Generated Patient ID: {P_id}")

#     # If photo capture is desired, capture the photo (photo processing is handled by PhotoComparator)
#     if add_photo == "y":
#         print("📸 Capturing photo...")
#         # Call your photo capture function here; for example, cap_photo(P_id)
#         # Assuming cap_photo(P_id) captures and saves a photo locally.
#         cap_photo(P_id)  # This function should capture and save the image in the expected folder.
#         # For record creation, we don't store the photo URL.
#         photo_path = f"IOT_relational_Database/patient_photos/{P_id}.jpg"

#     age = input("🔢 Enter age: ").strip()
#     medical_cond = input("🩺 Enter medical condition: ").strip()
#     Medicines = input("💊 Enter medicines (comma separated): ").split(',')
#     time_medicines = input("⏰ Enter time for medicines (comma separated): ").split(',')
#     Medicine_taken = input("✅ Is medicine taken? (yes/no): ").strip().lower() == "yes"

#     # Add the patient record (without storing the photo URL)
#     records.add_patient(P_id, pat_name, age, medical_cond, Medicines, time_medicines, Medicine_taken, photo_path)
