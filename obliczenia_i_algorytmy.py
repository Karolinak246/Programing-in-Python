################################
# 7.12.2020
# Kopczak Karolina
# Programowanie w jezyku Python
# Zadania: OBLICZENIA I ALGORYTMY
################################

#!/usr/bin/env python3
path = "/home/pi/Documents/Python"

import math
import random
import numpy as np

### TASK 1 ###
def square_equation():
	print ("a * x^2 + b * x + c")
	a = float(input("Write a: "))
	b = float(input("Write b: "))
	c = float(input("Write c: "))

	DELTA = b**2 - 4*a*c

	if DELTA < 0:
		print ("There is no sollution in real numbers")
	elif DELTA == 0:
		X1 = X2 = (-b/(2*a))
		print("\nThe answer","\nX1 = ", X1,"\nX2 = ",X2)
	else:
		X1 = (-b + (DELTA ** (1/2)))/(2*a)
		X2 = (-b - (DELTA ** (1/2)))/(2*a)
		print("\nThe answer","\nX1 = ", X1, "\nX2 = ", X2)

#square_equation()


### TASK 2 ###
def bubble_sort(tab):
	for i in range (len(tab)):
		j=len(tab)-1
		while (j > i):
			if tab[j-1]<tab[j]:
				tmp= tab[j]
				tab[j] = tab [j-1]
				tab[j-1] = tmp
			j=j-1
	return tab


def randnumb():
	print("Amount numbers to generate: 50")
	size = 50
	min = float(input("Minimum: "))
	max = float(input("Maximum: "))
	tab = []

	for i in range(size):
		tab.append(random.randrange(min, max))

	print("Generated numbers:","\n", tab)

	tab = bubble_sort(tab)

	print("Sorted numbers:","\n", tab)


#randnumb()

### TASK 3 ###
def twovect():
	a = [1, 2, 12, 4]
	b = [2, 4, 2, 8]
	c = []
	sum = 0

	for i in range (len(a)):
		c.append(a[i]*b[i])
		sum = sum + c[i]

	print("a = [1, 2, 12, 4]","\nb = [2, 4, 2, 8]\n\na * b =",sum)

#twovect()

### TASK 4 ###
def summatrix():
	A = np.random.randint(100, size = (128,128))
	B = np.random.randint(100, size = (128,128))
	SUM = np.zeros((128,128))

	for i in range(A.shape [0]):
		for j in range(A.shape[0]):
			SUM[i][j]=A[i][j]+B[i][j]
	print("Matrix A: \n",A,"\nMatrix B: \n",B,"\n\nSUMMARY: \n",SUM)

#summatrix()

### TASK 5 ###

def multimatrix():
	A = np.random.randint(100, size = (8,8))
	B = np.random.randint(100, size = (8,8))
	SUM = np.zeros((8,8))

	for i in range(A.shape [0]):
		for j in range(A.shape[0]):
			for f in range(A.shape[0]):
				SUM[i][j]=SUM[i][j]+A[i][f]*B[f][j]

	print("Matrix A: \n",A,"\nMatrix B: \n",B,"\n\nSUMMARY: \n",SUM)

#multimatrix()

### TASK 6 ###
def detmatrix():
	k = int(input("Size of MATRIX (n x n) Enter \"n\": "))
	A = np.random.randint(100, size = (k,k))
	detA = np.linalg.det(A)
	print("Matrix:\n",A,"\n\ndet A:\n",detA)

detmatrix()
