n = int(input("enter number"))

if n % 2 == 0:
    print('not weird')
else:
    print('weird')
if n % 2 == 0 and n <= 5:
    print("not weird")
if n % 2 == 0 and n == 6 or n < 20:
    print("weird")
if n % 2 == 0 and n > 20:
    print("not weird =")
