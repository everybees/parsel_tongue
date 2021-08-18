first_number= int(input("Enter first number\n"))
second_number=int(input("Enter second number\n"))
third_number=int(input("Enter third number\n"))

if (first_number>second_number or second_number>third_number):
    print(False)
else:
    if (first_number<second_number and second_number<third_number):
        print(True)




