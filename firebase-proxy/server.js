import express from "express";
import cors from "cors";
import fetch from "node-fetch";

const app = express();
app.use(cors());

const FIREBASE_URL = "https://vishwas-patra-default-rtdb.asia-southeast1.firebasedatabase.app/patients.json";

app.get("/patients", async (req, res) => {
    try {
        const response = await fetch(FIREBASE_URL);
        if (!response.ok) throw new Error(`HTTP error! Status: ${response.status}`);
        
        const data = await response.json();
        res.json(data);
    } catch (error) {
        console.error("Error fetching Firebase data:", error);
        res.status(500).json({ error: "Error fetching Firebase data" });
    }
});

const PORT = 5000;
app.listen(PORT, () => console.log(`Proxy server running on http://localhost:${PORT}/patients`));
