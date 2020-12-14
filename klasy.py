################################
# 7.12.2020
# Kopczak Karolina
# Programowanie w jezyku Python
# Zadania: KLASY
################################

#!/usr/bin/env python3

path = "/home/pi/Documents/Python"

import math

### TASK 1 ###
class Complex(object):
	def __init__(self, real, imag):
		self.real = real
		self.imag = imag

	def __add__(self, b):
		sum_real = self.real + b.real
		sum_imag = self.imag + b.imag
		return Complex(sum_real, sum_imag)

	def __diff__(self, b):
		diff_real = self.real - b.real
		diff_imag = self.imag - b.imag
		return Complex(diff_real, diff_imag)

	def __mult__(self, b):
		mult_real = self.real * b.real - self.imag * b.imag
		mult_imag = self.real * b.imag + self.imag * b.real
		return Complex(mult_real, mult_imag)

	def __abs__(self):
		abs = (self.real ** 2 + self.imag **2) ** (1/2)
		return abs


### TASK 2 ###
def calculator():
	print("Select an operation\n 1 - \"a + b\"\n 2 - \"a - b\"\n 3 - \"a * b\"\n 4 - \" |a| \"")
	operation = int(input("\nEnter number of operation (1 - 4): "))

########### 1 - "a + b" #############
########### 2 - "a - b" #############
########### 3 - "a * b" #############
########### 4 - " |a| " #############

	print("Now you have to enter two numbers and separate them by space (for Re and Im). For example:\na : 3 6    -  means a = 3 + 6j\nb : 8 1    -  means b = 8 + 1j" )
	if operation > 0 and operation < 4:
		temp1 = input("Enter \"a\": ")
		temp1Re, temp1Im = temp1.split(" ")
		TEMP1 = Complex(int(temp1Re), int(temp1Im))

		temp2 = input("Enter \"b\": ")
		temp2Re, temp2Im = temp2.split(" ")
		TEMP2 = Complex(int(temp2Re), int(temp2Im))

		if operation == 1:
			sum = Complex.__add__(TEMP1, TEMP2)
			print("Result: (" + str(sum.real) + ") + (" + str(sum.imag) + ")j")

		if operation == 2:
			diff = Complex.__diff__(TEMP1, TEMP2)
			print("Result: (" + str(diff.real) + ") + (" + str(diff.imag) + ")j")

		if operation == 3:
			mult = Complex.__mult__(TEMP1, TEMP2)
			print("Result: (" + str(mult.real) + ") + (" + str(mult.imag) + ")j")
	elif operation  == 4:
		temp = input("Enter \"a\": ")
		tempRe, tempIm = temp.split(" ")
		TEMP = Complex(int(tempRe), int(tempIm))
		ans = Complex.__abs__(TEMP)
		print("Result: " + str(ans.real))
	else:
		print("There is no such operation")

calculator()
