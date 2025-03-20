<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Patient Portal - MediCare Hospital</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        
        body {
            background-color: #f8f9fa;
            color: #333;
            line-height: 1.6;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
        }
        
        /* Header Styles */
        header {
            background-color: #2c3e50;
            color: white;
            padding: 1rem 0;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }
        
        .navbar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 20px;
        }
        
        .logo {
            font-size: 1.8rem;
            font-weight: 700;
            color: #ffffff;
            text-decoration: none;
        }
        
        .logo span {
            color: #3498db;
        }
        
        .nav-links {
            display: flex;
            list-style: none;
        }
        
        .nav-links li {
            margin-left: 30px;
        }
        
        .nav-links a {
            text-decoration: none;
            color: white;
            font-weight: 500;
            transition: color 0.3s;
        }
        
        .nav-links a:hover {
            color: #3498db;
        }
        
        /* Main Content */
        .main-content {
            flex: 1;
            max-width: 1200px;
            margin: 0 auto;
            padding: 2rem 20px;
            width: 100%;
        }
        
        /* Patient Info Header */
        .patient-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 2rem;
            padding-bottom: 1rem;
            border-bottom: 1px solid #ddd;
        }
        
        .patient-info h1 {
            font-size: 2rem;
            color: #2c3e50;
            margin-bottom: 0.5rem;
        }
        
        .patient-info p {
            color: #7f8c8d;
            font-size: 1.1rem;
        }
        
        .appointment-btn {
            padding: 12px 24px;
            background-color: #3498db;
            color: white;
            border: none;
            border-radius: 4px;
            font-size: 1rem;
            font-weight: 500;
            cursor: pointer;
            transition: background-color 0.3s;
        }
        
        .appointment-btn:hover {
            background-color: #2980b9;
        }
        
        /* Dashboard Cards */
        .dashboard {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
            gap: 1.5rem;
            margin-bottom: 2rem;
        }
        
        .card {
            background-color: white;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            padding: 1.5rem;
            transition: transform 0.3s, box-shadow 0.3s;
        }
        
        .card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 20px rgba(0,0,0,0.1);
        }
        
        .card-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 1rem;
            padding-bottom: 0.5rem;
            border-bottom: 1px solid #eee;
        }
        
        .card-title {
            font-size: 1.3rem;
            color: #2c3e50;
            font-weight: 600;
        }
        
        .card-badge {
            padding: 0.25rem 0.75rem;
            border-radius: 20px;
            font-size: 0.8rem;
            font-weight: 500;
        }
        
        .badge-blue {
            background-color: #e1f0fa;
            color: #3498db;
        }
        
        .badge-green {
            background-color: #e1f5eb;
            color: #2ecc71;
        }
        
        .badge-yellow {
            background-color: #fef5e5;
            color: #f39c12;
        }
        
        .badge-red {
            background-color: #fce5e5;
            color: #e74c3c;
        }
        
        .card-content {
            font-size: 0.95rem;
        }
        
        .data-item {
            margin-bottom: 0.75rem;
            display: flex;
        }
        
        .data-label {
            flex: 1;
            font-weight: 500;
            color: #7f8c8d;
        }
        
        .data-value {
            flex: 2;
            font-weight: 400;
        }
        
        /* Medical Records Section */
        .records-section {
            background-color: white;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            padding: 1.5rem;
            margin-bottom: 2rem;
        }
        
        .section-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 1.5rem;
            padding-bottom: 0.5rem;
            border-bottom: 1px solid #eee;
        }
        
        .section-title {
            font-size: 1.5rem;
            color: #2c3e50;
            font-weight: 600;
        }
        
        .table-container {
            overflow-x: auto;
        }
        
        table {
            width: 100%;
            border-collapse: collapse;
        }
        
        thead {
            background-color: #f8f9fa;
        }
        
        th, td {
            padding: 12px 15px;
            text-align: left;
            border-bottom: 1px solid #eee;
        }
        
        th {
            font-weight: 600;
            color: #2c3e50;
        }
        
        tbody tr:hover {
            background-color: #f8f9fa;
        }
        
        .status-pill {
            display: inline-block;
            padding: 0.25rem 0.75rem;
            border-radius: 20px;
            font-size: 0.8rem;
            font-weight: 500;
        }
        
        /* Footer */
        footer {
            background-color: #2c3e50;
            color: white;
            padding: 1rem 0;
            text-align: center;
            margin-top: auto;
        }
        
        /* Modal */
        .modal {
            display: none;
            position: fixed;
            z-index: 1000;
            left: 0;
            top: 0;
            width: 100%;
            height: 100%;
            background-color: rgba(0,0,0,0.5);
            overflow: auto;
        }
        
        .modal-content {
            background-color: white;
            margin: 10% auto;
            padding: 2rem;
            border-radius: 8px;
            max-width: 500px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.3);
            position: relative;
        }
        
        .close-btn {
            position: absolute;
            top: 20px;
            right: 20px;
            font-size: 1.5rem;
            font-weight: bold;
            color: #7f8c8d;
            cursor: pointer;
            transition: color 0.3s;
        }
        
        .close-btn:hover {
            color: #e74c3c;
        }
        
        .modal-title {
            font-size: 1.5rem;
            color: #2c3e50;
            margin-bottom: 1.5rem;
            padding-bottom: 0.5rem;
            border-bottom: 1px solid #eee;
        }
        
        .form-group {
            margin-bottom: 1.5rem;
        }
        
        label {
            display: block;
            margin-bottom: 0.5rem;
            font-weight: 500;
            color: #2c3e50;
        }
        
        .form-control {
            width: 100%;
            padding: 12px;
            border: 1px solid #ddd;
            border-radius: 4px;
            font-size: 1rem;
            transition: border-color 0.3s;
        }
        
        .form-control:focus {
            outline: none;
            border-color: #3498db;
        }
        
        .submit-btn {
            width: 100%;
            padding: 12px;
            background-color: #3498db;
            color: white;
            border: none;
            border-radius: 4px;
            font-size: 1rem;
            font-weight: 500;
            cursor: pointer;
            transition: background-color 0.3s;
        }
        
        .submit-btn:hover {
            background-color: #2980b9;
        }
        
        /* Responsive */
        @media (max-width: 768px) {
            .patient-header {
                flex-direction: column;
                align-items: flex-start;
            }
            
            .appointment-btn {
                margin-top: 1rem;
            }
            
            .dashboard {
                grid-template-columns: 1fr;
            }
            
            .nav-links {
                display: none;
            }
        }
    </style>
</head>
<body>
    <!-- Header -->
    <header>
        <nav class="navbar">
            <a href="index.html" class="logo">Medi<span>Care</span></a>
            <ul class="nav-links">
                <li><a href="patient-portal.html" class="active">Dashboard</a></li>
                <li><a href="#">Medical Records</a></li>
                <li><a href="#">Appointments</a></li>
                <li><a href="#">Messages</a></li>
                <li><a href="#">Profile</a></li>
                <li><a href="index.html">Logout</a></li>
            </ul>
        </nav>
    </header>

    <!-- Main Content -->
    <main class="main-content">
        <!-- Patient Header -->
        <div class="patient-header">
            <div class="patient-info">
                <h1>Welcome, <span id="patientName">John Doe</span></h1>
                <p>Patient ID: <span id="patientId">P123456</span> | Last Visit: <span id="lastVisit">March 15, 2025</span></p>
            </div>
            <button id="scheduleBtn" class="appointment-btn">Schedule Appointment</button>
        </div>
        
        <!-- Dashboard Cards -->
        <div class="dashboard">
            <!-- Personal Information -->
            <div class="card">
                <div class="card-header">
                    <h2 class="card-title">Personal Information</h2>
                    <span class="card-badge badge-blue">Profile</span>
                </div>
                <div class="card-content">
                    <div class="data-item">
                        <span class="data-label">Full Name:</span>
                        <span class="data-value" id="fullName">John Doe</span>
                    </div>
                    <div class="data-item">
                        <span class="data-label">Date of Birth:</span>
                        <span class="data-value" id="dob">January 15, 1980</span>
                    </div>
                    <div class="data-item">
                        <span class="data-label">Age:</span>
                        <span class="data-value" id="age">45</span>
                    </div>
                    <div class="data-item">
                        <span class="data-label">Gender:</span>
                        <span class="data-value" id="gender">Male</span>
                    </div>
                    <div class="data-item">
                        <span class="data-label">Contact:</span>
                        <span class="data-value" id="contact">(555) 123-4567</span>
                    </div>
                    <div class="data-item">
                        <span class="data-label">Email:</span>
                        <span class="data-value" id="email">john.doe@example.com</span>
                    </div>
                    <div class="data-item">
                        <span class="data-label">Address:</span>
                        <span class="data-value" id="address">123 Main St, Anytown, CA 12345</span>
                    </div>
                </div>
            </div>
            
            <!-- Vital Signs -->
            <div class="card">
                <div class="card-header">
                    <h2 class="card-title">Vital Signs</h2>
                    <span class="card-badge badge-green">Latest</span>
                </div>
                <div class="card-content">
                    <div class="data-item">
                        <span class="data-label">Height:</span>
                        <span class="data-value" id="height">5'10" (178 cm)</span>
                    </div>
                    <div class="data-item">
                        <span class="data-label">Weight:</span>
                        <span class="data-value" id="weight">175 lbs (79.4 kg)</span>
                    </div>
                    <div class="data-item">
                        <span class="data-label">BMI:</span>
                        <span class="data-value" id="bmi">25.1</span>
                    </div>
                    <div class="data-item">
                        <span class="data-label">Blood Pressure:</span>
                        <span class="data-value" id="bloodPressure">120/80 mmHg</span>
                    </div>
                    <div class="data-item">
                        <span class="data-label">Heart Rate:</span>
                        <span class="data-value" id="heartRate">72 bpm</span>
                    </div>
                    <div class="data-item">
                        <span class="data-label">Temperature:</span>
                        <span class="data-value" id="temperature">98.6°F (37°C)</span>
                    </div>
                    <div class="data-item">
                        <span class="data-label">Last Updated:</span>
                        <span class="data-value" id="vitalsDate">March 15, 2025</span>
                    </div>
                </div>
            </div>
            
            <!-- Current Medications -->
            <div class="card">
                <div class="card-header">
                    <h2 class="card-title">Current Medications</h2>
                    <span class="card-badge badge-yellow">Active</span>
                </div>
                <div class="card-content">
                    <div class="data-item">
                        <span class="data-label">Medication 1:</span>
                        <span class="data-value">Atorvastatin 20mg - Once daily</span>
                    </div>
                    <div class="data-item">
                        <span class="data-label">Medication 2:</span>
                        <span class="data-value">Lisinopril 10mg - Once daily</span>
                    </div>
                    <div class="data-item">
                        <span class="data-label">Medication 3:</span>
                        <span class="data-value">Metformin 500mg - Twice daily</span>
                    </div>
                    <div class="data-item">
                        <span class="data-label">Allergies:</span>
                        <span class="data-value">Penicillin, Sulfa drugs</span>
                    </div>
                    <div class="data-item">
                        <span class="data-label">Prescribing Doctor:</span>
                        <span class="data-value">Dr. Sarah Johnson</span>
                    </div>
                    <div class="data-item">
                        <span class="data-label">Last Reviewed:</span>
                        <span class="data-value">February 28, 2025</span>
                    </div>
                </div>
            </div>
            
            <!-- Upcoming Appointments -->
            <div class="card">
                <div class="card-header">
                    <h2 class="card-title">Upcoming Appointments</h2>
                    <span class="card-badge badge-blue">Scheduled</span>
                </div>
                <div class="card-content">
                    <div class="data-item">
                        <span class="data-label">Next Appointment:</span>
                        <span class="data-value">March 25, 2025 - 10:30 AM</span>
                    </div>
                    <div class="data-item">
                        <span class="data-label">Doctor:</span>
                        <span class="data-value">Dr. Sarah Johnson - Cardiology</span>
                    </div>
                    <div class="data-item">
                        <span class="data-label">Location:</span>
                        <span class="data-value">Main Hospital - Room 302</span>
                    </div>
                    <div class="data-item">
                        <span class="data-label">Reason:</span>
                        <span class="data-value">Follow-up appointment</span>
                    </div>
                    <div class="data-item">
                        <span class="data-label">Notes:</span>
                        <span class="data-value">Please bring your medication list</span>
                    </div>
                </div>
            </div>
        </div>
        
        <!-- Medical Records Section -->
        <div class="records-section">
            <div class="section-header">
                <h2 class="section-title">Recent Medical Records</h2>
            </div>
            <div class="table-container">
                <table>
                    <thead>
                        <tr>
                            <th>Date</th>
                            <th>Type</th>
                            <th>Doctor</th>
                            <th>Diagnosis</th>
                            <th>Status</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>March 15, 2025</td>
                            <td>Regular Checkup</td>
                            <td>Dr. Sarah Johnson</td>
                            <td>Hypertension, Type 2 Diabetes</td>
                            <td><span class="status-pill badge-green">Completed</span></td>
                        </tr>
                        <tr>
                            <td>February 12, 2025</td>
                            <td>Blood Test</td>
                            <td>Dr. Michael Chen</td>
                            <td>Routine monitoring</td>
                            <td><span class="status-pill badge-green">Completed</span></td>
                        </tr>
                        <tr>
                            <td>January 30, 2025</td>
                            <td>Cardiology Consultation</td>
                            <td>Dr. Sarah Johnson</td>
                            <td>Mild coronary artery disease</td>
                            <td><span class="status-pill badge-green">Completed</span></td>
                        </tr>
                        <tr>
                            <td>December 18, 2024</td>
                            <td>X-Ray</td>
                            <td>Dr. Robert Wilson</td>
                            <td>Chest X-ray - Normal</td>
                            <td><span class="status-pill badge-green">Completed</span></td>
                        </tr>
                        <tr>
                            <td>November 5, 2024</td>
                            <td>Endocrinology</td>
                            <td>Dr. Lisa Patel</td>
                            <td>Diabetes management</td>
                            <td><span class="status-pill badge-green">Completed</span></td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </main>

    <!-- Footer -->
    <footer>
        <p>&copy; 2025 MediCare Hospital. All rights reserved.</p>
    </footer>

    <!-- Appointment Modal -->
    <div id="appointmentModal" class="modal">
        <div class="modal-content">
            <span class="close-btn">&times;</span>
            <h2 class="modal-title">Schedule an Appointment</h2>
            <form id="appointmentForm">
                <div class="form-group">
                    <label for="specialty">Specialty</label>
                    <select id="specialty" class="form-control" required>
                        <option value="">Select a specialty</option>
                        <option value="cardiology">Cardiology</option>
                        <option value="dermatology">Dermatology</option>
                        <option value="endocrinology">Endocrinology</option>
                        <option value="neurology">Neurology</option>
                        <option value="orthopedics">Orthopedics</option>
                        <option value="primary">Primary Care</option>
                    </select>
                </div>
                <div class="form-group">
                    <label for="doctor">Doctor</label>
                    <select id="doctor" class="form-control" required>
                        <option value="">Select a doctor</option>
                    </select>
                </div>
                <div class="form-group">
                    <label for="appDate">Date</label>
                    <input type="date" id="appDate" class="form-control" required>
                </div>
                <div class="form-group">
                    <label for="appTime">Time</label>
                    <select id="appTime" class="form-control" required>
                        <option value="">Select a time</option>
                    </select>
                </div>
                <div class="form-group">
                    <label for="reason">Reason for Visit</label>
                    <textarea id="reason" class="form-control" rows="3" required></textarea>
                </div>
                <button type="submit" class="submit-btn">Schedule Appointment</button>
            </form>
        </div>
    </div>

    <!-- Firebase SDK -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/firebase/9.22.0/firebase-app-compat.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/firebase/9.22.0/firebase-auth-compat.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/firebase/9.22.0/firebase-firestore-compat.js"></script>
    <script src="firebase.js"></script>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            // Get DOM elements
            const modal = document.getElementById('appointmentModal');
            const scheduleBtn = document.getElementById('scheduleBtn');
            const closeBtn = document.querySelector('.close-btn');
            const specialtySelect = document.getElementById('specialty');
            const doctorSelect = document.getElementById('doctor');
            const dateInput = document.getElementById('appDate');
            const timeSelect = document.getElementById('appTime');
            const appointmentForm = document.getElementById('appointmentForm');
            
            // Get database reference
            const db = firebase.firestore();
            const auth = firebase.auth();
            
            // Load patient data from Firestore
            function loadPatientData() {
                // Get patient ID from session storage (set during login)
                const patientId = sessionStorage.getItem('patientId');
                
                if (patientId) {
                    db.collection('patients').doc(patientId).get()
                        .then((doc) => {
                            if (doc.exists) {
                                const patientData = doc.data();
                                
                                // Update UI with patient information
                                document.getElementById('patientName').textContent = patientData.name || 'Patient';
                                document.getElementById('patientId').textContent = patientData.patientId || 'Unknown';
                                document.getElementById('fullName').textContent = patientData.name || 'Unknown';
                                document.getElementById('dob').textContent = patientData.dob || 'Unknown';
                                document.getElementById('age').textContent = patientData.age || 'Unknown';
                                document.getElementById('gender').textContent = patientData.gender || 'Unknown';
                                document.getElementById('contact').textContent = patientData.phone || 'Unknown';
                                document.getElementById('email').textContent = patientData.email || 'Unknown';
                                document.getElementById('address').textContent = patientData.address || 'Unknown';
                                
                                // Load vital signs if available
                                if (patientData.vitals) {
                                    document.getElementById('height').textContent = patientData.vitals.height || 'Not recorded';
                                    document.getElementById('weight').textContent = patientData.vitals.weight || 'Not recorded';
                                    document.getElementById('bmi').textContent = patientData.vitals.bmi || 'Not recorded';
                                    document.getElementById('bloodPressure').textContent = patientData.vitals.bloodPressure || 'Not recorded';
                                    document.getElementById('heartRate').textContent = patientData.vitals.heartRate || 'Not recorded';
                                    document.getElementById('temperature').textContent = patientData.vitals.temperature || 'Not recorded';
                                    document.getElementById('vitalsDate').textContent = patientData.vitals.date || 'Unknown';
                                }
                                
                                // Load medical records
                                loadMedicalRecords(patientId);
                            } else {
                                console.error("No patient document found!");
                                // Redirect to login if patient data not found
                                window.location.href = 'index.html';
                            }
                        })
                        .catch((error) => {
                            console.error("Error fetching patient data:", error);
                        });
                } else {
                    console.error("No patient ID found in session!");
                    // Redirect to login if no patient ID
                    window.location.href = 'index.html';
                }
            }
            
            // Load patient's medical records
            function loadMedicalRecords(patientId) {
                db.collection('medicalRecords')
                    .where('patientId', '==', patientId)
                    .orderBy('date', 'desc')
                    .limit(5)
                    .get()
                    .then((querySnapshot) => {
                        const recordsTableBody = document.querySelector('tbody');
                        recordsTableBody.innerHTML = ''; // Clear existing records
                        
                        if (querySnapshot.empty) {
                            // No records found
                            const row = document.createElement('tr');
                            row.innerHTML = '<td colspan="5">No medical records found.</td>';
                            recordsTableBody.appendChild(row);
                        } else {
                            querySnapshot.forEach((doc) => {
                                const record = doc.data();
                                const row = document.createElement('tr');
                                
                                // Format date
                                const recordDate = record.date ? record.date.toDate() : new Date();
                                const formattedDate = recordDate.toLocaleDateString('en-US', {
                                    year: 'numeric',
                                    month: 'long',
                                    day: 'numeric'
                                });
                                
                                row.innerHTML = `
                                    <td>${formattedDate}</td>
                                    <td>${record.type || 'Unknown'}</td>
                                    <td>${record.doctor || 'Unknown'}</td>
                                    <td>${record.diagnosis || 'Not specified'}</td>
                                    <td><span class="status-pill badge-${record.status === 'Completed' ? 'green' : 'yellow'}">${record.status || 'Unknown'}</span></td>
                                `;
                                
                                recordsTableBody.appendChild(row);
                            });
                        }
                    })
                    .catch((error) => {
                        console.error("Error fetching medical records:", error);
                    });
            }
            
            // Show modal
            scheduleBtn.addEventListener('click', function() {
                modal.style.display = 'block';
                
                // Set minimum date to today
                const today = new Date();
                const formattedDate = today.toISOString().split('T')[0];
                dateInput.setAttribute('min', formattedDate);
                
                // Clear previous selections
                doctorSelect.innerHTML = '<option value="">Select a doctor</option>';
                timeSelect.innerHTML = '<option value="">Select a time</option>';
            });
            
            // Close modal
            closeBtn.addEventListener('click', function() {
                modal.style.display = 'none';
            });
            
            // Close modal when clicking outside
            window.addEventListener('click', function(event) {
                if (event.target === modal) {
                    modal.style.display = 'none';
                }
            });
            
            // Handle specialty selection
            specialtySelect.addEventListener('change', function() {
                const specialty = this.value;
                
                if (specialty) {
                    // Fetch doctors by specialty
                    db.collection('doctors')
                        .where('specialty', '==', specialty)
                        .get()
                        .then((querySnapshot) => {
                            // Clear previous options
                            doctorSelect.innerHTML = '<option value="">Select a doctor</option>';
                            
                            querySnapshot.forEach((doc) => {
                                const doctor = doc.data();
                                const option = document.createElement('option');
                                option.value = doc.id;
                                option.textContent = `Dr. ${doctor.name} - ${doctor.specialty}`;
                                doctorSelect.appendChild(option);
                            });
                        })
                        .catch((error) => {
                            console.error("Error fetching doctors:", error);
                        });
                } else {
                    // Clear doctor select if no specialty selected
                    doctorSelect.innerHTML = '<option value="">Select a doctor</option>';
                }
            });
            
            // Handle date selection
            dateInput.addEventListener('change', function() {
                const selectedDate = this.value;
                const doctorId = doctorSelect.value;
                
                if (selectedDate && doctorId) {
                    // Fetch available times for the selected doctor and date
                    // This part is missing in the original code and needs to be implemented
                }
            });
            
            // // Handle appointment form submission
            // appointmentForm.addEventListener('submit', function(event) {
            //     event.preventDefault();
            //     // Handle appointment scheduling logic here
            //     // This part is also missing in the original code and needs to be implemented
            // });
            // #######################################################
            appointmentForm.addEventListener('submit', function(e) {
                e.preventDefault();
                // ... (Retrieve form values)
            
                if (patientId && doctorId && appDate && appTime && reason) {
                    db.collection('appointments').add({
                        // ... (Appointment data)
                    }).then(() => {
                        alert('Appointment scheduled successfully!');
                        modal.style.display = 'none';
                    }).catch((error) => {
                        console.error('Error scheduling appointment:', error);
                        if(error.code === 'permission-denied'){
                            alert('You do not have permission to schedule an appointment. Please contact support.');
                        } else{
                            alert('Failed to schedule appointment. Please try again.');
                        }
            
                    });
                } else {
                    alert('Please fill in all fields.');
                }
            });
        }
        
    </script>
</body>
</html>
