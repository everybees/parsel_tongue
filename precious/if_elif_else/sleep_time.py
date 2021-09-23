A = int(input("Enter Number \n"))
B = int(input("Enter Number \n"))
H = int(input("Enter Number \n"))
if H < A:
    print("Deficiency")
elif H > B:
    print("Excess")
elif H > A < B:
    print("Normal")
