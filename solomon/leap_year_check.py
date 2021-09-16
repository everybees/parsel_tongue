# print("Leap" if int(input("Enter year") % 4 == 0 and int(input()) % 400 != 0) else "Ordinary")
year = int(input("Enter year: "))
if year % 4 == 0 and year % 100 != 0 or year % 400 ==0:
    print("Leap")
else:
    print("Ordinary")
