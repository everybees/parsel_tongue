year = int(input("enter year"))

if year % 4 and year % 100 == 0 or year % 400 == 0:
    print("its a leap year")
else:
    print("ordinary")

    if year % 400 == 0:
        print("its a leap year")
