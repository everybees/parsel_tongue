#  As seen in Abdulfatai's repo
import time

def BMI():
	weight = int(input("Enter Weight in kilograms: "))
	height = float(input("Enter Height in meters: "))
	return weight / height**2

def multiplier():
	first_number = int(input("Enter first number:"))
	second_number = int(input("Enter second number:"))
	return first_number * second_number


print("Your fucking BMI is:", BMI())
time.sleep(3)
print("The result is: ", multiplier())
