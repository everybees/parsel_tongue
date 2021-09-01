x_axis = int(input()) 
y_axis = int(input()) 
if x_axis == 0 and y_axis == 0:
    print('its the origin')
elif x_axis < 0 and y_axis < 0:
    print('III quadrant')
elif x_axis > 0 and y_axis > 0:
    print('I quadrant')
elif x_axis < 0 and y_axis > 0:
    print('II quadrant')
elif x_axis > 0 and y_axis < 0:
    print('IV quadrant')

