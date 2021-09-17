# # leap_ year
year = int(input("Enter the year\n"))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("Leap")
else:
    print("Ordinary")

# else_statement

number_1 = int(input("Enter the first Number\n"))
number_2 = int(input("Enter the second Number\n"))

maximum = max(number_1, number_2)
minimum = min(number_1, number_2)
print("maximun is: ", maximum)
print("maximun is: ", minimum)

number_1 = int(input("Enter the first Number\n"))
number_2 = int(input("Enter the second Number\n"))

minimum = min(number_1, number_2)
maximum = max(number_1, number_2)
print("minimum is: ", minimum)
print("maximun is: ", maximum)