X = float(input("Enter the value of X\n"))

Y = float(input("Enter the value of Y\n"))

if 1 <= X <= 10 and -10 <= Y <= 0:
    print("IV")

elif 1 <= X <= 10 and 1 <= Y <= 10:
    print("I")

elif -10 <= X <= 0 and 1 <= Y <= 10:
    print("II")

elif -10 <= X <= 0 and -10 <= Y <= 0:
    print("III")
