year = int(input())
print("Leap"if year % 4==0 and year % 100 != 0 or year % 400 == 0  else "Ordinary")
   






first = int(input())
second = int(input())

maximum = first
if second > maximum:
    print()
    print(second)
    print(first)
    print()
else:
    print(first)
    print(second)   
    
