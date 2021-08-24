x_axis = int(input("Please Enter A Number for X Axis\n"))
y_axis = int(input("Please Enter A Number for Y Axis\n"))
if(x_axis > 0 and y_axis > 0):
    print("Coordinate is I")
elif(x_axis > 0 and y_axis < 0):
        print("Coordinate is IV")
elif(x_axis < 0 and y_axis <0):
        print("Coordinate is III")
elif(x_axis < 0 and y_axis > 0):
                print("Coordinate is II")
elif(x_axis == y_axis):
                print("Origin")