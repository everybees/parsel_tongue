#leap year check
year = int(input("Enter the year:"))
if (year % 4 and year % 100) == 0 and year % 400 == 0:
    print("Leap")
else:
    print("Ordinary")
    
#minimum and maximum
first_number = int(input("First number: "))
second_number = int(input("Second number: "))

maximum = first_number
if second_number >  maximum:
    print(second_number)
    print(maximum)
else:
    print(maximum)
    print(second_number)


