x = float(input("Enter a point on the cartesian coordinate:"))
y = float(input("Enter a point on the cartesian coordinate:"))

if x == 0 and y == 0:
    print("it's the origin!" )
elif y == 0:
    print(f"({x}, {y}) is on the x-axis")
elif x == 0:
    print(f" ({x},{y}) is on the y-aixs")
elif y > 0:
    if x > 0:
        print(f"({x},{y}) is in the first quadrant")
    else:
        print(f"({x},{y}) is in the second quadrant")
else:
    print(f"({x},{y}) is in the third quadrant")
else: 
print(f"({x},{y}) is in the fouth quadrant")






