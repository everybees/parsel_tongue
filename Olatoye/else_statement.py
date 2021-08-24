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

def weirdo():
	number = int(input("Enter your number: "))
	
	if(number % 2 != 0 or (6 <= number <= 20 and number % 2 ==0)):
		print("Weird!")
	else:
		print("Not Weird!")
		
  weirdo()

def leap():
	year = int(input("Enter year: "))
	print("It is a leap year" if (year % 4 == 0 and year % 100 != 0) or year % 400 ==0 else "It is not a leap year")
	
  leap()

def comparison_again():
	num1 = int(input())
	num2 = int(input())
	
	print(f"\n{num1}\n{num2}" if num1 > num2 else f"{num2}\n{num1}")
	
comparison_again()
