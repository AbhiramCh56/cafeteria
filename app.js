import { initializeApp } from "https://www.gstatic.com/firebasejs/11.1.0/firebase-app.js";
import { getAnalytics } from "https://www.gstatic.com/firebasejs/11.1.0/firebase-analytics.js";

const firebaseConfig = {
  apiKey: "AIzaSyBcEQij-CZbi-4tkn7ZmSPcLafsN64E3ok",
  authDomain: "canteen-40419.firebaseapp.com",
  projectId: "canteen-40419",
  storageBucket: "canteen-40419.firebasestorage.app",
  messagingSenderId: "952353215885",
  appId: "1:952353215885:web:a2edee3c0726e4c458d9c4",
  measurementId: "G-JG4ZXYX95Y",
};
const app = initializeApp(firebaseConfig);
const analytics = getAnalytics(app);

firebase.initializeApp(firebaseConfig);
const db = firebase.firestore();
const storage = firebase.storage();

const feedbackForm = document.getElementById("feedbackForm");

feedbackForm.addEventListener("submit", async (e) => {
  e.preventDefault();

  const issue = document.getElementById("issue").value.trim();
  const name = document.getElementById("name").value.trim();
  const photo = document.getElementById("photo").files[0];

  if (issue === "") {
    alert("Please mention your issue before submitting.");
    return;
  }

  let photoURL = "";
  if (photo) {
    const storageRef = storage.ref(`feedback_photos/${photo.name}`);
    await storageRef.put(photo);
    photoURL = await storageRef.getDownloadURL();
  }

  try {
    await db.collection("feedbacks").add({
      issue,
      name: name || "Anonymous",
      photoURL,
      timestamp: firebase.firestore.FieldValue.serverTimestamp(),
    });
    alert(`Thank you ${name || "Anonymous"} for your feedback!`);
    feedbackForm.reset();
  } catch (error) {
    console.error("Error adding feedback: ", error);
    alert("Error submitting feedback. Please try again.");
  }
});
