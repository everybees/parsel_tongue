#leap year
year = int(input())

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("Leap")
else:
    print("Ordinary")

#maximum of two numbers
first_number = int(input())
second_number = int(input())

if second_number > first_number:
    print (second_number)
    print(first_number)
else:
    print(first_number)
    print(second_number)