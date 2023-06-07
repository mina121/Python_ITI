for row in range (1,7,1):
	print("\t\t\t",end='')
	for x in range (1,row,1):
		print(" ",end='')
	for y in range (0,(14-(2*row)-1),1):
		print("*",end='')
	print("")