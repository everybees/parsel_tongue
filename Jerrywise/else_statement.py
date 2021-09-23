year_enter = int(input("Number of years: "))
if (year_enter % 4 == 0 and year_enter % 100 != 0) or year_enter % 400 == 0:
    print("it is a leap year")
else:
    print("it is ordinary")
