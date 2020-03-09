from PIL import Image
import os, sys

for files in os.listdir("./know"):
	if files[-4:]=="jpeg":		
		im = Image.open("./know/"+files)
		bg = im.convert("RGB")
		print(files)
		bg.save("./know/"+files[:-4]+"jpg")
		os.remove("./know/"+files)
