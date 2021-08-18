n=int(input())
if n % 2 != 0:
    print("Weird")
if n % 2 == 0 and 2 <= n <=5:
    print("Not weird")
if n % 2 == 0 and 6 <= n <=20:
    print("Weird")
if n % 2 == 0 and n > 20:
    print("Not weird")
               
