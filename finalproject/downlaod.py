import pyrebase


config = {
  "apiKey": "AIzaSyDZFaXexrptFx5dGnLnG04SApyS9N-Vb_c",
  "authDomain": "faceattendance-89125.firebaseapp.com",
  "databaseURL": "https://faceattendance-89125.firebaseio.com",
  "projectId": "faceattendance-89125",
  "storageBucket": "faceattendance-89125.appspot.com",
  "messagingSenderId": "1088230635859"
}


firebase = pyrebase.initialize_app(config)

storage = firebase.storage()

storage.child("faceimage.jpg").download("faceimage.jpg")



storage.child("faceimage.jpg").remove()


