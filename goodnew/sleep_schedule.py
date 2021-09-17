A = int(input("Enter the recommended sleep hour\n"))
B = int(input("Enter the max sleep hour\n"))
H = int(input("Enter your sleep hours\n"))

if H < A:
    print("Deficient")
elif H > A:
    print("Excess")
elif H >= A and H <= B:
    print("Normal")