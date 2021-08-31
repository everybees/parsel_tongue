for i in range(int(input("Enter a number:"))):
    for j in range(i + 1):
       print("*", end="")
    print()

for i in range(10):
    for j in range(10 - i):
      print("*", end="")
    print()