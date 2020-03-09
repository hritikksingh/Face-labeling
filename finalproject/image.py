from firebase import firebase
from google.cloud import storage
import cv2
import numpy as np

firebase=firebase.FirebaseApplication('https://faceattendance-89125.firebaseio.com/')
client=storage.Client()
bucket=client.get_bucket('faceattendance-89125.appspot.com')

for idX in range(1,len(result)):	
	for imageY in range(0,64):
		pathWay='dataSet/User'+str(idX)+'.'+str(imageY)
		print(pathWay)
		imageBlob=bucket.blob(pathWay)
		print(imageBlob)
		url=imageBlob.publib_url
		req=urllib.urlopen(url)
		arr=np.asarray(bytearray(req.raed()),dtype=np.uint8)
		img=cv2.imdecoder(arr,-1)
