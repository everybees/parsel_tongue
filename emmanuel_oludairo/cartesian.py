x_axis = float(input())
y_axis = float(input())

if x_axis < 0 and y_axis > 0:
    print("II")
elif x_axis == 0 and y_axis == 0:
    print("It's the origin")
elif x_axis > 0 and y_axis > 0:
    print("I")
elif x_axis > 0 and y_axis < 0:
    print("IV")
else:
    print("III")
