// Import Firebase modules correctly (for Firebase v9+)
import { initializeApp } from "https://www.gstatic.com/firebasejs/9.23.0/firebase-app-compat.js";
import { getDatabase } from "https://www.gstatic.com/firebasejs/9.23.0/firebase-database-compat.js";

// Firebase configuration
const firebaseConfig = {
    apiKey: "AIzaSyDxl02vves6dluwcqKGuKNq9f9Sgkszbb8",
    authDomain: "vishwas-patra.firebaseapp.com",
    databaseURL: "https://vishwas-patra-default-rtdb.asia-southeast1.firebasedatabase.app",
    projectId: "vishwas-patra",
    storageBucket: "vishwas-patra.firebasestorage.app",
    messagingSenderId: "276926459600",
    appId: "1:276926459600:web:d773473ad7a5152076b8d5",
    measurementId: "G-830Q37LQ11"
};

// Initialize Firebase (prevent duplicate initialization)
const app = initializeApp(firebaseConfig);
const database = getDatabase(app);

// Export database to use in other files
export { database };
