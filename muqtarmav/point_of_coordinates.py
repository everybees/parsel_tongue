
x = float(input("enter first coordinate: "))
y = float(input("enter second coordinate: "))


if x > 0 and y > 0:
        print("I")
elif x < 0 and y > 0:
    print("II")
elif x < 0 and y < 0:
    print("III")
elif x == 0.0 or y == 0.0:
    print("one of the coordinates is equal to zero")
elif x > 0 and y < 0:
    print("IV")









#else:
   # print("its the origin")

