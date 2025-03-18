import cv2
import numpy as np
import face_recognition
import time
import os
import patient_db

class FaceRecog:
    def __init__(self):
        self.known_face_encodings = []
        self.known_face_names = []
        self.video_capture = None

    def load_known_faces(self, photo_directory="IOT_relational_Database/patient_photos"):
        """Load known face images from a directory and generate encodings."""
        known_faces = []

        if not os.path.exists(photo_directory):
            print(f"⚠️ Directory not found: {photo_directory}")
            return False

        for filename in os.listdir(photo_directory):
            if filename.endswith(".jpg"):
                img_path = os.path.join(photo_directory, filename)
                label = os.path.splitext(filename)[0]
                known_faces.append((img_path, label))

        for image_path, name in known_faces:
            try:
                image = face_recognition.load_image_file(image_path)
                face_locations = face_recognition.face_locations(image)
                face_encodings = face_recognition.face_encodings(image, face_locations)

                if face_encodings:
                    self.known_face_encodings.append(face_encodings[0])
                    self.known_face_names.append(name)
                else:
                    print(f"⚠️ Warning: No face detected in {image_path}")
            except Exception as e:
                print(f"Error loading {image_path}: {e}")

        return len(self.known_face_encodings) > 0

    def initialize_webcam(self):
        """Initialize the webcam with a lower resolution."""
        self.video_capture = cv2.VideoCapture(0)
        if not self.video_capture.isOpened():
            print("❌ Error: Could not open webcam.")
            return False

        self.video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, 160)
        self.video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 120)
        return True

    def process_frame(self, frame):
        """Process a frame for face detection and recognition."""
        scale_factor = 0.5
        small_frame = cv2.resize(frame, (0, 0), fx=scale_factor, fy=scale_factor)
        rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

        face_locations = face_recognition.face_locations(rgb_small_frame, model='hog')
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding)
            name = "Unknown"
            if any(matches):
                face_distances = face_recognition.face_distance(self.known_face_encodings, face_encoding)
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = self.known_face_names[best_match_index]
            face_names.append(name)

        

        return frame, face_names,face_locations

    def main(self):
        """Run face recognition in a loop until 'q' is pressed."""
        if not self.load_known_faces():
            print("⚠️ No valid face encodings loaded. Exiting...")
            return

        if not self.initialize_webcam():
            return

        prev_time = time.time()
        process_this_frame = True

        try:
            while True:
                ret, frame = self.video_capture.read()
                if not ret:
                    continue

                current_time = time.time()
                elapsed_time = current_time - prev_time
                if elapsed_time > 0:
                    fps = 1 / elapsed_time
                else:
                    fps = 0
                prev_time = current_time
                # Track already processed IDs
                processed_faces = set()
                
                if process_this_frame:
                    frame, face_names,face_locations = self.process_frame(frame)
                    
                    pat = patient_db.MedicalRecords()  # Initialize outside the loop for efficiency
                    
                    for id_face in face_names:
                        if id_face not in processed_faces:  # Only process new faces
                            print(f"Processing ID: {id_face}")
                            pat.get_patients_withPid(id_face)
                            processed_faces.add(id_face)  # Mark as processed
                        else:
                            print(f"Skipping already processed ID: {id_face}")        
                process_this_frame = not process_this_frame
                
                scale_factor = 0.5
                scale_back = int(1 / scale_factor)
                for (top, right, bottom, left), name in zip(face_locations, face_names):
                    top *= scale_back
                    right *= scale_back
                    bottom *= scale_back
                    left *= scale_back
                    cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 150), 2)
                    cv2.putText(frame, name, (left, top - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 150), 2)
                cv2.putText(frame, f"FPS: {fps:.2f}", (10, 30),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
                cv2.imshow("Real-Time Face Recognition", frame)

                # Small sleep to prevent CPU overuse and ZeroDivisionError
                time.sleep(0.001)

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
        except KeyboardInterrupt:
            print("\n⏹️ Stopped by user (Ctrl+C).")
        finally:
            self.video_capture.release()
            cv2.destroyAllWindows()
            print("🛑 Webcam closed. Exiting.")

if __name__ == "__main__":
    FaceRecog().main()
