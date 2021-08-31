A = int(input("Enter sleep hour:"))
B = int(input("Enter sleep hour:"))
H = int(input("Enter sleep hour:"))

if H < A:
    print("Deficiency")
elif H > B:
    print("Excess")
elif H >= A and H <= B:
    print("Normal")

