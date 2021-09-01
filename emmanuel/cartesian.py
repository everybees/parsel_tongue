X = float(input("X axis: "))
Y = float(input("Y axis: "))

if X == 0 and Y == 0:
    print("It's the origin")
elif X > 0 and Y > 0:
    print("I")
elif X > 0 and Y < 0:
    print("IV")
elif X < 0 and Y > 0:
    print("II")
elif X == 0 or Y == 0:
    print("One of the coordinate is zero")
else:
    print("III")

