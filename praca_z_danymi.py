################################
# 7.12.2020
# Kopczak Karolina
# Programowanie w jezyku Python
# Zadania: PRACA Z DANYMI
################################

#!/usr/bin/env python3

path = "/home/pi/Documents/Python"
from xml.dom import minidom
import xml.dom.minidom
import os
import pandas as pd
import numpy as np
import csv 

### TASK 1 ###
def xml():
	file = minidom.parse("XML/somexml.xml")
	tag = file.getElementsByTagName("CATALOG")[0]
	print("Tag name before changing: ", file.firstChild.tagName)
	tag.tagName = "change"
	file.writexml(open('XML/some_changed_xml.xml', 'w'))
	file2 = minidom.parse("XML/some_changed_xml.xml")
	print("Tag name after changing: ", file2.firstChild.tagName)

xml()

### TASK 2 ###
def csvjson():
	if os.path.isfile("CSV/file.csv")==True:
		try:
			data = pd.read_csv("CSV/file.csv")
			print(data)
			deleterecord = input ("Would you like to delete last record? Y/N ")
			if deleterecord == "y" or deleterecord == "Y":
				data.drop(data.tail(1).index, inplace = True)
				print (data)
				data.to_csv("CSV/file.csv", sep ="\t")
		except:
			print("The file is empty, data will be added.")
			data = pd.DataFrame()
	else:
		print("There is no file at such name. file.csv will be created.")

	newrecord = input("Would you like to add new record? Y/N ")

	if newrecord == "y" or newrecord == "Y":
		recA = input("Enter the title of the movie: ")
		recB = input("Enter the code of CD: ")
		recC = input("Enter Client's name: ")
		recD = input("Enter Clinet's surname: ")
		recE = input("Enter phone number: ")
		recF = input("Enter amount of days (how long will the film be on loan?): ")
		recG = input("Enter the price: ")

		df = pd.DataFrame({	"Title":[recA],
					"Code":[recB],
					"Name":[recC],
					"Surname":[recD],
					"Phone_number":[recE],
					"Days":[recF],
					"Price":[recG]})
		if data.empty == True:
			df.to_csv("CSV/file.csv", sep = "\t", header = True)
		else:
			df.to_csv("CSV/file.csv", sep = "\t", mode = "a", header = False)
csvjson()
