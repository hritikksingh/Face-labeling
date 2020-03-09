import os,sys




if os.stat('./unknown/prev.jpg').st_size==os.stat('./unknown/current.jpg').st_size:
	print("lol ho gaya")

else:
	print("chuttad")
