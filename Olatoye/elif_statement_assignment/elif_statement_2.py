def elif_statement_2():
	x = int(input("Enter x coordinate: "))
	y = int(input("Enter y coordinate: "))
	print("\n")
	
	if x > 0 and y > 0:
		print("I")
	elif x < 0 and y > 0:
		print("II")
	elif x < 0 and y < 0:
		print("III")
	elif x > 0 and y < 0:
		print("IV")
	elif x == 0 and y == 0:
		print("It's the origin!")
	elif x == 0 or y == 0:
		print("One of the coordinates is equal to zero")
		
elif_statement_2()

