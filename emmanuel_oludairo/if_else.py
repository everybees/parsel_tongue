n = int(input("Enter number: "))

if n % 2 > 0:
    print("Weird")
elif n % 2 == 0 and 2 <= n <= 5:
    print("Not Weird")
elif n % 2 == 0 and 6 <= n <= 20:
    print("Weird")
elif n % 2 == 0 and n > 20:
    print("Not weird")


first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))
if second_number > first_number:
    print("second_number is maximum" "\n" "first_number is minimum")
else:
    print("first_number is maximum" "\n" "second_number is minimum")
