year = int(input("Enter year\n"))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("leap year")
else:
    print("ordinary")


print("leap" if int(input()) % 4 == 0 and int(input()) % 100 != 0 or int(input()) / 400 == 0 else "ordinary")


first_number = int(input("enter first number \n"))
second_number = int(input("enter second number \n"))

maximum = max(first_number, second_number)
print(maximum)

minimum = min(first_number, second_number)
print(minimum)



