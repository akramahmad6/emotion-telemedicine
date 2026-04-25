import { initializeApp } from "https://www.gstatic.com/firebasejs/12.12.1/firebase-app.js";
import { getDatabase } from "https://www.gstatic.com/firebasejs/12.12.1/firebase-database.js";

const firebaseConfig = {
  apiKey: "AIzaSyC1jyVCVwbYWZTMDLmiqQop8lmB4kZErZc",
  authDomain: "emotion-telemedicine.firebaseapp.com",
  databaseURL: "https://emotion-telemedicine-default-rtdb.firebaseio.com",
  projectId: "emotion-telemedicine",
  storageBucket: "emotion-telemedicine.firebasestorage.app",
  messagingSenderId: "26308050974",
  appId: "1:26308050974:web:bdbf0ace02321bf1b5ee0f"
};

const app = initializeApp(firebaseConfig);
const db = getDatabase(app);

export { db };