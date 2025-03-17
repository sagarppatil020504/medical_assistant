import cv2
import numpy as np
import face_recognition
import time
import os

class face_recog:
    def __init__(self):
        self.known_face_encodings = []
        self.known_face_names = []
        self.video_capture = None


    def load_known_faces(self, photo_directory="IOT_relational_Database/patient_photos"):
        """Load known face images from a directory and generate encodings."""
        
        known_faces = []
        
        # Ensure the directory exists
        if not os.path.exists(photo_directory):
            print(f"⚠️ Directory not found: {photo_directory}")
            return known_faces

        # Loop through all .jpg files in the directory
        for filename in os.listdir(photo_directory):
            if filename.endswith(".jpg"):
                img_path = os.path.join(photo_directory, filename)
                label = os.path.splitext(filename)[0]  # Remove .jpg extension
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
        """Initialize the webcam with a lower resolution to reduce memory usage."""
        self.video_capture = cv2.VideoCapture(0)
        if not self.video_capture.isOpened():
            raise RuntimeError("Error: Could not open webcam.")
        
        # Set to a lower resolution (e.g., 160x120)
        self.video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, 160)
        self.video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 120)
        return True
    
    def process_frame(self, frame):
        """
        Process a single frame to detect and recognize faces.
        Downscale the frame by 0.5 for faster processing, then scale coordinates back up.
        """
        scale_factor = 0.5  # Downscale factor for processing
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
        
        # Draw bounding boxes and labels on the original frame.
        # Since we processed a frame scaled by 0.5, multiply coordinates by 1/0.5 = 2.
        scale_back = int(1/scale_factor)
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            top *= scale_back
            right *= scale_back
            bottom *= scale_back
            left *= scale_back
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 150), 2)
            cv2.putText(frame, name, (left, top - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 150), 2)
        
        return frame, face_names
    
    def main(self):
        """Run face recognition continuously until 'q' is pressed."""
        if not self.load_known_faces():
            print("No valid face encodings loaded. Exiting...")
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
                fps = 1 / (current_time - prev_time) if (current_time - prev_time) > 0 else 0
                prev_time = current_time
                
                if process_this_frame:
                    frame, face_names = self.process_frame(frame)
                    if face_names:
                        print("Detected Faces:", face_names)
                
                process_this_frame = not process_this_frame
                
                cv2.putText(frame, f"FPS: {fps:.2f}", (10, 30),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
                cv2.imshow("Real-Time Face Recognition", frame)
                
                # Exit loop if 'q' is pressed.
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
        except KeyboardInterrupt:
            pass
        finally:
            self.video_capture.release()
            cv2.destroyAllWindows()

if __name__ == "__main__":
    face_recog().main()



# import cv2
# import numpy as np
# import face_recognition
# import time

# class face_recog:
#     def __init__(self):
#         self.known_face_encodings = []
#         self.known_face_names = []
#         self.video_capture = None
        
#     def load_known_faces(self):
#         """Load known face images and generate encodings"""
#         known_faces = [("sagar.jpg", "Sagar 1")]
        
#         for image_path, name in known_faces:
#             try:
#                 image = face_recognition.load_image_file(image_path)
#                 face_locations = face_recognition.face_locations(image)
#                 face_encodings = face_recognition.face_encodings(image, face_locations)
                
#                 if face_encodings:
#                     self.known_face_encodings.append(face_encodings[0])
#                     self.known_face_names.append(name)
#                 else:
#                     print(f"⚠️ Warning: No face detected in {image_path}")
#             except Exception as e:
#                 print(f"Error loading {image_path}: {e}")
        
#         return len(self.known_face_encodings) > 0
    
#     def initialize_webcam(self):
#         """Initialize the webcam"""
#         self.video_capture = cv2.VideoCapture(0)
#         if not self.video_capture.isOpened():
#             raise RuntimeError("Error: Could not open webcam.")
        
#         self.video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, 240)
#         self.video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 180)
#         return True
    
#     def process_frame(self, frame):
#         """Process a single frame to detect and recognize faces"""
#         small_frame = cv2.resize(frame, (0, 0), fx=0.75, fy=0.75)
#         rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)
        
#         face_locations = face_recognition.face_locations(rgb_small_frame, model='hog')
#         face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
        
#         face_names = []
#         for face_encoding in face_encodings:
#             matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding)
#             name = "Unknown"

#             if any(matches):
#                 face_distances = face_recognition.face_distance(self.known_face_encodings, face_encoding)
#                 best_match_index = np.argmin(face_distances)
#                 if matches[best_match_index]:
#                     name = self.known_face_names[best_match_index]
            
#             face_names.append(name)
        
#         # Draw bounding boxes and labels
#         for (top, right, bottom, left), name in zip(face_locations, face_names):
#             # Scale back up face locations since the frame we detected in was scaled
#             top *= 2
#             right *= 2
#             bottom *= 2
#             left *= 2
            
#             cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 150), 2)
#             cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 150), 2)
        
#         return frame, face_names
    
#     def main(self):
#         """Main function to run face recognition continuously until 'q' is pressed"""
#         if not self.load_known_faces():
#             print("No valid face encodings loaded. Exiting...")
#             return []
        
#         if not self.initialize_webcam():
#             return []
        
#         prev_time = time.time()
#         process_this_frame = True
#         detected_faces = []
        
#         try:
#             while True:
#                 # Capture frame-by-frame
#                 ret, frame = self.video_capture.read()
#                 if not ret:
#                     continue
                
#                 current_time = time.time()
#                 fps = 1 / (current_time - prev_time) if (current_time - prev_time) > 0 else 0
#                 prev_time = current_time
                
#                 if process_this_frame:
#                     frame, face_names = self.process_frame(frame)
#                     if face_names:
#                         detected_faces = face_names
#                         print("Detected Faces:", face_names)
                
#                 process_this_frame = not process_this_frame
                
#                 # Display FPS on the frame
#                 cv2.putText(frame, f"FPS: {fps:.2f}", (10, 30), 
#                             cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
                
#                 cv2.imshow("Real-Time Face Recognition", frame)
                
#                 # Break the loop on 'q' key press
#                 if cv2.waitKey(1) & 0xFF == ord('q'):
#                     break
#         except KeyboardInterrupt:
#             pass
#         finally:
#             # Release the webcam and close all windows
#             self.video_capture.release()
#             cv2.destroyAllWindows()
            
#         return detected_faces

# if __name__ == "__main__":
#     face_recog().main()










# import cv2
# import numpy as np
# import face_recognition
# import threading
# import queue
# import time

# stop_event = threading.Event()
# recognized_faces_queue = queue.Queue()

# def load_known_faces():
#     """Load known face images and generate encodings"""
#     known_faces = [("sagar.jpg", "Sagar 1")]
#     known_face_encodings = []
#     known_face_names = []
    
#     for image_path, name in known_faces:
#         image = face_recognition.load_image_file(image_path)
#         face_locations = face_recognition.face_locations(image)
#         face_encodings = face_recognition.face_encodings(image, face_locations)
        
#         if face_encodings:
#             known_face_encodings.append(face_encodings[0])
#             known_face_names.append(name)
#         else:
#             print(f"⚠️ Warning: No face detected in {image_path}")
    
#     return known_face_encodings, known_face_names

# def initialize_webcam():
#     """Initialize the webcam"""
#     video_capture = cv2.VideoCapture(0)
#     if not video_capture.isOpened():
#         raise RuntimeError("Error: Could not open webcam.")
    
#     video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, 240)
#     video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 180)
#     return video_capture

# def capture_frames(video_capture, frame_queue):
#     """Continuously capture frames from the webcam"""
#     while not stop_event.is_set():
#         ret, frame = video_capture.read()
#         if not ret:
#             continue

#         if frame_queue.full():
#             frame_queue.get_nowait()  # Remove old frame
        
#         frame_queue.put(frame)
#         time.sleep(0.01)

# def process_frames(frame_queue, known_face_encodings, known_face_names):
#     """Detect and recognize faces in frames, then store recognized names"""
#     process_this_frame = True
#     prev_time = time.time()
    
#     while not stop_event.is_set():
#         try:
#             frame = frame_queue.get(timeout=1)
#         except queue.Empty:
#             continue

#         current_time = time.time()
#         fps = 1 / (current_time - prev_time) if (current_time - prev_time) > 0 else 0
#         prev_time = current_time

#         small_frame = cv2.resize(frame, (0, 0), fx=0.65, fy=0.45)
#         rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

#         face_names = []
        
#         if process_this_frame:
#             face_locations = face_recognition.face_locations(rgb_small_frame, model='hog')
#             face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
            
#             # print(f"Detected Face Locations: {face_locations}")  # Debugging Output
            
#             for face_encoding in face_encodings:
#                 matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
#                 name = "Unknown"

#                 if any(matches):
#                     face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
#                     best_match_index = np.argmin(face_distances)
#                     if matches[best_match_index]:
#                         name = known_face_names[best_match_index]
                
#                 face_names.append(name)
        
#         process_this_frame = not process_this_frame

#         if face_names:
#             recognized_faces_queue.put(face_names)

#         # Draw Bounding Boxes (Fixing Scaling)
#         for (top, right, bottom, left), name in zip(face_locations, face_names):
#             top *=2;right *=2; left *=2; bottom *=2
#             cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
#             cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

#         cv2.putText(frame, f"FPS: {fps:.2f}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
#         cv2.imshow("Real-Time Face Recognition", frame)

#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             stop_event.set()
#             break

# class face_recog:
#     def main(self):

#         known_face_encodings, known_face_names = load_known_faces()
#         if not known_face_encodings:
#             print("No valid face encodings loaded. Exiting...")
#             return

#         video_capture = initialize_webcam()
#         frame_queue = queue.Queue(maxsize=1)

#         capture_thread = threading.Thread(target=capture_frames, args=(video_capture, frame_queue), daemon=True)
#         processing_thread = threading.Thread(target=process_frames, args=(frame_queue, known_face_encodings, known_face_names), daemon=True)

#         capture_thread.start()
#         processing_thread.start()

#         try:
#             while not stop_event.is_set():
#                 try:
#                     face_names = recognized_faces_queue.get(timeout=0.1)
#                     print("Detected Faces:", face_names)
#                     return face_names
#                 except queue.Empty:
#                     pass
#         except KeyboardInterrupt:
#             stop_event.set()
#         finally:
#             capture_thread.join()
#             processing_thread.join()
#             video_capture.release()
#             cv2.destroyAllWindows()

# if __name__ == "__main__":
#     face_recog().main()
