A = int(input("minimum hours of sleep: "))
B = int(input("maximum hours of sleep: "))
H = int(input("hours of sleep per day: "))

if H < A:
    print("Deficiency")
elif H > B:
    print("Excess")
else:
    print("Normal")
