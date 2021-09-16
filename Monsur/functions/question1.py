import math

def max_of_three_numbers():

    value1 = int(input("Enter value 1: "))
    value2 = int(input("Enter value 2: "))
    value3 = int(input("Enter value 3: "))

    max_value = value1
    if value2 > max_value:
        max_value = value2
    if value3 > max_value:
        max_value = value3
    print("maximum number is : ", max_value)







