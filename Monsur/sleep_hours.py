
A_hours = int(input("Enter value of a: "))
B_hours = int(input("Enter value of b: "))
H_hours = int(input("Enter value of h: "))

if H_hours < A_hours:
    print("deficiency")
elif H_hours > B_hours:
    print("excess")
elif A_hours < H_hours < B_hours:
    print("normal")