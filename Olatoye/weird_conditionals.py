def weirdo():
	number = int(input("Enter your number: "))
	
	if(number % 2 != 0 or (6 <= number <= 20 and number % 2 ==0)):
		print("Weird!")
	else:
		print("Not Weird!")
		
weirdo()
