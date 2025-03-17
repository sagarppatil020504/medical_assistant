import queue
import connector_reco_db
import patient_db

# Global task queue (if used by worker_db, otherwise remove if not needed)
task_queue = queue.Queue()

def main():
    
    while True:
        print("Select Mode:")
        print("1. Monitor Condition (Face Recognition)")
        print("2. Staff Work (Patient Database Operations)")
        print("3. Exit")
        choice = input("Enter your choice (1 or 2): ").strip()

        if choice == "1":
            print("press q to exit")
            face_con = connector_reco_db.face_recognition()  # Ensure this is the correct class name in your module
            pat = patient_db.MedicalRecords()
            pat.get_patients_withPid(face_con)
            # face_con.main()
            main()
            
        elif choice == "2":
            password = input("Enter password: ").strip()
            if password == "65":
                staff_con = connector_reco_db.MedicalRecordsConnector()
                staff_con.main()
                main()
            else:
                print("Wrong password")
                main()
                
        elif choice == "3":
            print("Exiting.")
            break
        else :
            break

if __name__ == "__main__":
    main()
