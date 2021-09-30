x_axis = float(input())
y_axis = float(input())

def coordinates():

    if x_axis < 0 and y_axis > 0:
        print("II")
    elif x_axis == 0 and y_axis == 0:
        print("Its the origin")
    elif x_axis > 0 and y_axis < 0:
        print("IV")
    elif x_axis < 0 and y_axis < 0:
        print("III")
    elif x_axis == 0 or y_axis == 0:
        print("One of the coordinate is zero")
    else:
        print("I")
