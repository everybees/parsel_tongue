coordinate_x = float (input("Enter first coordinate point: "))
coordinate_y = float (input("Enter second coordinate point: "))

if coordinate_x!=0 and coordinate_y!=0:
    if coordinate_x > 0 and coordinate_y > 0:
        print("I")
    elif coordinate_x < 0 and coordinate_y > 0:
        print("II")
    elif coordinate_x < 0 and coordinate_y < 0:
        print("III")
    else:
        print("IV")
elif coordinate_x == 0 or coordinate_y == 0:
    print("One of the coordinates is equal to zero!")
else:
    print("Its the origin!")
        