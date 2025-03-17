while True:
        print("Select Mode:")
        print("1. Monitor Condition (Face Recognition)")
        print("2. Staff Work (Patient Database Operations)")
        print("3. Exit")
        choice = input("Enter your choice (1 or 2): ").strip()

        if choice == "1":
            print("press q to exit")
            face_con = connector_reco_db.face_recognition()  # Ensure this is the correct class name in your module
            face_con.main()
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