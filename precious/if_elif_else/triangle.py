print("the triangle is valid" if int(input()) + int(input()) + int(input()) == 180 else "invalid triangle")

triangle_angle_one = int(input("Enter first angle \n"))
triangle_angle_two = int(input("Enter second angle \n"))
triangle_angle_three = int(input("Enter third angle \n"))
if triangle_angle_one + triangle_angle_two + triangle_angle_three == 180:
    print("the triangle is valid")
else:
    print("invalid triangle")
