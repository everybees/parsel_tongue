def read_aloud():
	phone_number = input("Enter your phone number: ")
	
	try:
		number = int(phone_number)
	except:
		print("Enter digits only")
		read_aloud()
	
	for number in phone_number:
		print(number)
		
read_aloud()
