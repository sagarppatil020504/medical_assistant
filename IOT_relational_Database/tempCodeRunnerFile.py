        def task():
            patients = self.ref.get()
            if patients:
                for key, data in patients.items():
                    if data.get('P_id') == P_id:
                        result_queue.put(data)  # Store result in the queue
                        return
            result_queue.put(None)  # No patient found

        task_queue.put(task)
        result = result_queue.get()  # Wait for the task to complete

        if result:
            print("\n📋 Patient Details:")
            print(f"🆔 Patient ID: {result['P_id']}")
            print(f"👤 Name: {result['pat_name']}")
            print(f"🔢 Age: {result.get('age', 'N/A')}")
            print(f"🩺 Condition: {result['medical_cond']}")
            print(f"💊 Medicines: {', '.join(result.get('Medicines', []))}")
            print(f"⏰ Medicine Time: {', '.join(result.get('time_medicines', []))}")
            print(f"✅ Medicine Taken: {'Yes' if result.get('Medicine_taken', False) else 'No'}")
        else:
            print("⚠️ No patient found with the given ID.")


