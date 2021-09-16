import math

def test_range(number):
    if number in range(3, 9):
        print(number, "is in range")
    else:
        print("The number is outside the given range.")