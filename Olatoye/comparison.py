def comparison():
	num1 = int(input("Enter first number: "))
	num2 = int(input("Enter second number: "))
	
	if(num1 < num2):
		num3 = int(input("Enter third number: "))
		if(num2 < num3):
			print("They are in ascending order")
		else:
			print("They are not in ascending order")
	else:
		print("They are not in ascending order")
		
comparison()
