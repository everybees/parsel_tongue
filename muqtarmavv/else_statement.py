year = int(input("enter year"))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("its a leap year")
else:
    print("ordinary")


#MaximumOfTwoNumbers
number1 = int(input("enter first number"))
number2 = int(input("enter second number"))


maximum = number1

if (number2 > maximum):
    maximum = number2
    print(maximum)
else:
    print(number1)
