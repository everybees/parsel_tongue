# Question 3
import math
def product_of_numbers_in_a_list():
    x = int(input("Enter first range: "))
    y = int(input("Enter last range: "))

    list = []
    product = 1
    for a in range(x,y):
        user = int(input("Input Number: "))
        list.append(user)
    product 
    for b in list:
        product *= b
    print(product)