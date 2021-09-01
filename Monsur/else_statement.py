#leap year
year = int(input("Enter number of years: "))

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("leap")
else:
    print("ordinary")

#max of 2 numbers

number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))

if number1 > number2:
    print(number1)
    print(number2)
else:
    print(number2)
    print(number1)
