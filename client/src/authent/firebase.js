import firebase from "firebase";
import "firebase/firestore"

// Import the functions you need from the SDKs you need
// import { initializeApp } from "firebase/app";
// import { getAnalytics } from "firebase/analytics";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyDfof7h9zO-W1doNO-dqPpEP3AB_SOmkCQ",
  authDomain: "testrunz.firebaseapp.com",
  projectId: "testrunz",
  storageBucket: "testrunz.appspot.com",
  messagingSenderId: "637877304473",
  appId: "1:637877304473:web:bde4d4992ef5bff34e8c08",
  measurementId: "${config.measurementId}"
};

// Initialize Firebase 
const firebaseApp = firebase.initializeApp(firebaseConfig);
// const analytics = getAnalytics(app);
const db = firebaseApp.firestore();
const auth = firebase.auth(); 
const provider = new firebase.auth.GoogleAuthProvider();

export {auth, provider};
export default db;




// import firebase from "firebase";
// import "firebase/firestore"

// const firebaseConfig = {
//   apiKey: "AIzaSyCq0FCAOcRbwArd_4svCAYV7W0ymCSNzXM",
//   authDomain: "clamp-studio.firebaseapp.com",
//   databaseURL: "https://clamp-studio-default-rtdb.firebaseio.com",
//   projectId: "clamp-studio",
//   storageBucket: "clamp-studio.appspot.com",
//   messagingSenderId: "593234043253",
//   appId: "1:593234043253:web:62911102deadf57da1333c",
//   measurementId: "G-0TKQWWVCG2"
// };

// const firebaseApp = firebase.initializeApp(firebaseConfig);

// const db = firebaseApp.firestore();
// const auth = firebase.auth(); 
// const provider = new firebase.auth.GoogleAuthProvider();

// export {auth, provider};
// export default db;