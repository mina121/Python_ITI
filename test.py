def Add(x,y):
	return x + y 
def Sub(x,y):
	return x - y 
def Multi(x,y):
	return x * y 
def Div(x,y):
	return x / y 
print("*****************************************************************************")
print("Select Operation ")
print("1.Add")
print("2.SUbtract")
print("3.Multiply")
print("4.Division")
print("*****************************************************************************")

while True:
	choice=input("Enter Choice Your Choice : ") 
	print("*************************************************************************")
	if choice in ('1','2','3','4'):
		try:
			x=float(input("Enter First Number: "))
			y=float(input("\nEnter Second Number: "))
		except ValueError:
			print("Invalid Input. Try again")
			continue
		if choice == '1':
			print(x,"+",y,"=",Add(x,y))
		elif choice == '2':
			print(x,"-",y,"=",Sub(x,y))
		elif choice == '3':
			print(x,"*",y,"=",Multi(x,y))
		elif choice == '4':
			print(x,"/",y,"=",Div(x,y))
		next_op=input("Another Operation -->> (yes - no) : ")
		if next_op=="no":
			print("***********************GodBye********************")
			break
	else:
		print("invalid input")
