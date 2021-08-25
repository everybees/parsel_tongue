def read_aloud():
	numbers = ["zero", "one", "two", "three", "four", "four", "five", "six", "seven", "eight", "nine"]
	phone_number = input("Enter your phone number: ")
	
	try:
		number = int(phone_number)
	except:
		print("Enter digits only")
		read_aloud()
	
	for digit in phone_number:	
		print(numbers[int(digit)])
		
read_aloud()

