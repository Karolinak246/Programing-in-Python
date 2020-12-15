################################
# 7.12.2020
# Kopczak Karolina
# Programowanie w jezyku Python
# Zadania: PRACA Z PLIKAMI
################################

#!/usr/bin/env python3
path = "/home/pi/Documents/Python"

import os
from PIL import Image

### TASK 1 ###
def files_counter():
	os.chdir('/dev')
	files = os.listdir()
	print("In the /dev folder there is {} files.".format(len(files)))

files_counter()

### TASK 2 ###
def catalog():
	start = os.path.abspath(".")
	for root, dirs, files in os.walk(start):
		level =  root.replace(start, " ").count(os.sep)
		indent = " " * 3 * (level)
		print("{}{}/".format(indent, os.path.basename(root)))
		nextindent = " " * 3 * (level + 1)
		for f in files:
			print("{}{}".format(nextindent, f))

catalog()

### TASK 3 ###
def jpg_to_png_converter():
	images_location = '/home/pi/Documents/Python/Images'
	for f in os.listdir(images_location):
		if f.endswith("jpg"):
			jpg_image = Image.open(images_location+"/"+f)
			jpg_image.convert('RGB').save(images_location+ '/'+f.split(".")[0]+".png","PNG")

jpg_to_png_converter()
