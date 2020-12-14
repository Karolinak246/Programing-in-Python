################################
# 6.12.2020
# Kopczak Karolina
# Programowanie w jezyku Python
# Zadania: WEJSCIE/WYJSCIE
################################

#!/usr/bin/env python3

path = "/home/pi/Documents/Python"

### TASK 1 ###
def hello_world():
	print ("Hello World!")

hello_world()

### TASK 2 ###
def name_surname_year():
	name = input ("Enter your name: \n")
	surname = input ("Enter your surname: \n")
	year = input ("Enter your year of birth: \n")
	print ("\nSaved data:")
	print ("Name: ",name, " Surname: ", surname, " Year of birth: ", year)

name_surname_year()

### TASK 3 ###
def lock():
	password = 1234
	entercode = input("Enter code: ")
	if str(password) == entercode:
		print ("Your code is correct!")
	else:
		print ("Yore code is incorrect :c !")

lock()
