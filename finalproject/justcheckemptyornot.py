import os,sys

file=0
for file in os.listdir("./know/"):
	if file:	
		print("file is there\n")
	elif file==False:
		print("empty")
	elif file==0:
		print("null is working")
	else:	
		print("nothing")

