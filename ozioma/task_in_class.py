# Given an integer n, perform the following conditional actions:
# if n is odd, print weird
# if n is even and in the inclusive range of 2 and 5 print not weird
# if n is even and in the inclusive range of 6 to 20 print weird
# if n is even and greater than 20 print not weird
# input format - #A single line containing a positive integer n
# Constraints are -1 <= n <= 100
# output format print weird if the number is weird otherwise print not weird

n = int(input("Type a number: "))
if n % 2 != 0:
    print("weird")
if n % 2 == 0:
    if 2 <= n <= 5:
        print("not weird")
        if 6 <= n <= 20:
            print("weird")
            if n > 20:
                print("not weird")
