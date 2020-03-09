import face_recognition
import os,sys
from PIL import Image
import numpy as np


known_faces=[]
known_encodings=[]
results=[]
unknown_encodings=[]

unknown_image = face_recognition.load_image_file("12.jpeg")
face_locations=face_recognition.face_locations(unknown_image)



for face_location in face_locations:
	top,right,bottom,left=face_location
	face_image=unknown_image[top:bottom,left:right]
	enhanced=face_recognition.face_encodings(face_image)
	if len(enhanced)!=0:
		np.vstack(enhanced[0])

print(enhanced)

print(unknown_encodings)
	


for files in os.listdir("./know"):
	encodes=face_recognition.face_encodings(face_recognition.load_image_file("./know/"+files))[0]
	for unko in unknown_encodings:
		for i in unko:	
			results.append(face_recognition.compare_faces([encodes],i,tolerance=0.5))


"""
face_locations = face_recognition.face_locations()
face_encodings = face_recognition.face_encodings(face_locations)
matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
best_match_index = np.argmin(face_distances)
if matches[best_match_index]:
name = known_face_names[best_match_index]"""

	




