# Question 2
import math
def sum_of_numbers_in_a_list():

    x = int(input("Enter first range: "))
    y = int(input("Enter last range: "))

    list = []
    sum = 0
    for a in range(x,y):
        user = int(input("Input Number: "))
        list.append(user)
    for b in list:
        sum += b
    print(sum)