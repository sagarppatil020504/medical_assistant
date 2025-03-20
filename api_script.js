document.addEventListener("DOMContentLoaded", function () {
    const apiUrl = "http://localhost:5000/patients"; // Replace with your API endpoint

    const patName = document.getElementById("patName");
    const patId = document.getElementById("patId");
    const patAge = document.getElementById("patAge");
    const medCondition = document.getElementById("medCondition");
    const medicinesTaken = document.getElementById("medicinesTaken");
    const timeMedicines = document.getElementById("medicineTimings");
    const medicines = document.getElementById("medicinesToTake");

    const loadingIndicator = document.getElementById("loadingIndicator");
    const patientDetails = document.getElementById("patientDetails");
    const errorMessage = document.getElementById("errorMessage");

    // Ask the user for P_id input
    const patientId = prompt("Enter Patient ID:");

    if (!patientId) {
        alert("No Patient ID provided. Fetching aborted.");
        return;
    }

    fetch(apiUrl)
        .then(response => response.json())
        .then(data => {
            alert("Fetched Data: " + JSON.stringify(data, null, 2));

            loadingIndicator.style.display = "none";

            if (typeof data === "object" && data !== null) {
                const patient = data[patientId];

                if (patient) {
                    console.log("Matched Patient Data:", patient);
                    patientDetails.style.display = "block";

                    // Populate patient details
                    patName.textContent = patient.pat_name;
                    patId.textContent = patient.P_id;
                    patAge.textContent = patient.age;
                    medCondition.textContent = patient.medical_cond;
                    medicinesTaken.textContent = patient.Medicine_taken ? "Yes" : "No";
                    timeMedicines.textContent = patient.time_medicines || "Not Available";
                    medicines.textContent = patient.Medicines ? patient.Medicines.join(", ") : "No Medicines";
                } else {
                    errorMessage.style.display = "block";
                    errorMessage.textContent = "Error: Patient ID not found.";
                }
            } else {
                errorMessage.style.display = "block";
                errorMessage.textContent = "Error: Invalid response format.";
            }
        })
        .catch(error => {
            loadingIndicator.style.display = "none";
            errorMessage.style.display = "block";
            errorMessage.textContent = "Error fetching patient data. Please try again later.";
            console.error("Fetch error:", error);
        });
});
