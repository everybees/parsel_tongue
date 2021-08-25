year = int(input())

if (year % 4 == 0 and year % 100 != 0) or year % 400 ==0:
    print("Leap")
else:
    print("Ordinary")  


first = int(input())
second = int(input("\n"))

maximum = first

if second > maximum:
    print("\n",+second)
    print("\n",+first)
else:
    print(first,"\n")
    print(second,"\n")
