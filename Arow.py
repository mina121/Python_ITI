import os

from time import sleep

def Right_Arrow():
	for i in range (0,7,1):
		print("\t\t\t\t\t")
	for row in range (0,6,1):
		print("\t\t\t\t\t",end='')
		for x in range (0,row,1):
			print("*",end='')
		print("")
	print("\t\t\t**********************")

	for row in range (0,6,1):
		print("\t\t\t\t\t",end='')
		for x in range(row,5,1):
			print("*",end='')
		print("")
		
def Left_Arrow():

	for i in range (0,7,1):
		print("\t")
	for row in range (1,6,1):
		print("\t ",end='')
		for x in range(row,5,1):
			print(' ',end='')
		for z in range (0,row,1):
			print("*",end='')
		print("")
		
	print("\t************************")

	for row in range (1,6,1):
		print("\t ",end='')
		for x in range (1,row,1):
	 		print(' ',end='')
		for z in range (row,6,1):
			print("*",end='')
		print("")
		
		
		
def Up_Arrow():
	for i in range(0,5,1):
		print("\t\t\t\t")
	for row in range (0,6,1):
		print("\t\t\t\t",end='')
		for x in range (row,5,1):
			print(' ',end='')
		for z in range(0,2*row-1,1):
			print("*",end='')
			
		print("") 
	for i in range (0,7,1):
		print("\t\t\t\t    *")
def Down_Arrow():
	for i in range (0,6,1):
		print("\t\t\t")
	for c in range (0,7,1):
		print("\t\t\t     *")
	for row in range (1,7,1):
		print("\t\t\t",end='')
		for x in range (1,row,1):
			print(" ",end='')
		for y in range (0,(14-(2*row)-1),1):
			print("*",end='')
		print("")
		
		
while True:
	Up_Arrow()
	sleep(0.5)
	os.system('cls')
	Right_Arrow()
	sleep(0.5)
	os.system('cls')
	Down_Arrow()
	sleep(0.5)
	os.system('cls')
	Left_Arrow()
	sleep(0.5)
	os.system('cls')