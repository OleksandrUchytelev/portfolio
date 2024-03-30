
  import { initializeApp } from "https://www.gstatic.com/firebasejs/10.10.0/firebase-app.js";
  import { getAnalytics } from "https://www.gstatic.com/firebasejs/10.10.0/firebase-analytics.js";

  const firebaseConfig = {
    apiKey: "AIzaSyD9OS04FB7A1Op9wggU1n2eGg7eAWKaJZ0",
    authDomain: "portfolio-b17f9.firebaseapp.com",
    projectId: "portfolio-b17f9",
    storageBucket: "portfolio-b17f9.appspot.com",
    messagingSenderId: "189139724503",
    appId: "1:189139724503:web:a54d02c61e87318268e892",
    measurementId: "G-KJM7VLWYY4"
  };

  const app = initializeApp(firebaseConfig);
  const analytics = getAnalytics(app);