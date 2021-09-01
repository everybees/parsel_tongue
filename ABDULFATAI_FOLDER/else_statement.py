
#1. leap_year 
year = int(input())
if (year % 4 == 0 and year % 100 != 0) or (year % 400== 0):
    print("Ordinary")
else:
    
  print("Leap")
  
 #2. finding maximum and minimum number   
number1 = int(input())
number2 = int(input())

maximum = number1

if  number2 > maximum:
    print(number2)
    print(number1)

else:
    minimum = number2
    print(number2)


