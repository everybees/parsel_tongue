X_Coordinate = int(input("Enter Coordinate One: \n"))
Y_Coordinate = int(input("Enter Coordinate Two: \n"))

if X_Coordinate > 0 and Y_Coordinate < 0:
    print("IV")
elif X_Coordinate < 0 and Y_Coordinate > 0:
    print("II")
elif X_Coordinate < 0 and Y_Coordinate < 0:
    print("III")
elif X_Coordinate > 0 and Y_Coordinate > 0:
    print("I")
elif X_Coordinate == 0 and Y_Coordinate == 0:
    print("its the origin")
elif X_Coordinate == 0 or Y_Coordinate == 0:
    print("One of the coordinates is equal to zero")


