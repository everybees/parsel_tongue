number1 = int(input("first number: "))
number2 = int(input("second number: "))

if number1 >= 1 and number2 >= 1:
    print("I")
elif number1 >= 0 and number2 < 1:
    print("IV")
elif number1 < 0 and number2 >= 1:
    print("II")
else:
    print("III")

