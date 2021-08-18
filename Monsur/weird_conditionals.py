N = int(input("Enter number: "))

if N % 2 == 1:
    print("Weird")
if N % 2 == 0 and 2 >= N <= 5:
    print("Not Weird")
if N % 2 == 0 and 6 >= N <= 20:
    print("Weird")
if N % 2 == 0 and N > 20:
    print("Not Weird")
