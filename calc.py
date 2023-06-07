
import os

f1=open("file2.txt","a+")
		
def Add(x,y):
	return x + y 
def Sub(x,y):
	return x - y 
def Multi(x,y):
	return x * y 
def Div(x,y):
	return x / y 
while True:	
	print("***********************************************************************************")
	print("--------------------> Calculator For seintific and Programming <-------------------")
	print("***********************************************************************************")

	print("<--> For Sientific Mode Enter (s) <-->")
	print("***********************************************************************************")

	print("<--> For Programming Mode Enter (p) <-->")
	print("***********************************************************************************")
    
	choice=input("<--> Enter Mode <--> ")
	print("***********************************************************************************")

	dic1={"Add":1,"Sub":2,"Multi":3,"Div":4}
	dic2={"Oct":1,"Hex":2,"Bin":3,"Dec":4}

	if choice == 's':
		print("-------------------------> Welcome To Seintific Mode <-------------------------")
		print("For Summition Operation Enter --> (Add) <-- ")
		print("*******************************************************************************")

		print("For Subtraction Operation Enter --> (Sub) <-- ")
		print("*******************************************************************************")

		print("For Multiplication Operation Enter --> (Multi) <-- ")
		print("*******************************************************************************")

		print("For Division Operation Enter --> (Div) <-- ")
		print("*******************************************************************************")

		z=input("<-- Enter The Operation --> " )
		print("*******************************************************************************")
       # f1.write(z)
		x=int(input("<-- Enter The First Number --> "))
		
		print("*******************************************************************************")

		y=int(input("<-- Enter The Second Number --> "))
		print("*******************************************************************************")
		
		check=dic1[z]
		
		if check ==1:
			#print(x,"+",y,"=",Add(x,y))
			f1.write(int(Add(x,y)))
		elif check ==2:
			#print(x,"-",y,"=",Sub(x,y))
			f1.write(Sub(x,y))
		elif check ==3:
			#print(x,"*",y,"=",Multi(x,y))
			f1.write(Multi(x,y))
		elif check ==4:
			#print(x,"/",y,"=",Div(x,y))
			f1.write(Div(x,y))
			
			f1.open("file1.txt","r")
			print(f1.read())
			f1.close()
	elif choice == 'p':
		print("-------------------------> Welcome To Programming Mode <-------------------------")
		print("choose Format Of The Number ")
		print("For Octal Enter --> (O) <-- ")
		print("For Hexa Enter --> (H) <-- ")
		print("For Binnary Enter --> (B) <-- ")
		print("For Decimal Enter --> (D) <-- ")
		
		c=input("<-- Enter Your Choice --> ")
		num=input("<-- Enter The Number --> ")
		if c=='O':
			x=int(num,base=8)
		elif c=='H':
			x=int(num,base=16)
		elif c=='B':
			x=int(num,base=2)
		elif c=='D':
			x=int(num)
		else:
			print("Invalid Choice")
		print("Select The Format Of The Output Number")
		print("*******************************************************************************")

		print("For Getting Octal Representation Enter --> (Oct) <-- ")
		print("*******************************************************************************")

		print("For Getting Hexa Representation Enter --> (Hex) <-- ")
		print("*******************************************************************************")

		print("For Getting Binnary Representation Enter --> (Bin) <-- ")
		print("*******************************************************************************")

		print("For Getting Decimal Representation Enter --> (Dec) <-- ")
		print("*******************************************************************************")

		
		z=input("<-- Select your Operation --> ")
		print("*******************************************************************************")

		check=dic2[z]
		
		if check ==1:
			print("The Octal -->>"+str(oct(x)))
		elif check ==2:
			print("The Hexa -->>"+str(hex(x)))
		elif check ==3:
			print("The Binnary -->>"+str(bin(x)))
		elif check ==4:
			print("The Decimal -->>"+str(x))
		else:
			print("Invalid choice")
    
	
	
		