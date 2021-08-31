x_coordinate = float(input("Enter the value for x coordinate "))
y_coordinate = float(input("Enter the value for y coordinate "))
if(x_coordinate == 0 and y_coordinate == 0):
    print("It's the origin")
elif(x_coordinate > 0 and y_coordinate > 0):
    print("I")
elif(x_coordinate < 0 and y_coordinate > 0):
    print("II")
elif(x_coordinate > 0 and y_coordinate < 0):
    print("IV")
elif(x_coordinate < 0 and y_coordinate < 0):
    print("III")
else:
    print("One of the coordinates is equal to zero")
    
