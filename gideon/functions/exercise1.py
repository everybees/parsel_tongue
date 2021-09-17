#Question 1
# import math
def max_of_three_numbers():

    print("Enter three numbers to find the max")

    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = int(input("Enter third number: "))
    return max(a, b, c)

# Question 2
import math
def sum_of_numbers_in_a_list():

    print("Enter range and numbers to find the sum of numbers in a list")

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

# Question 3
import math
def product_of_numbers_in_a_list():

    print("Enter range and numbers to find the product of numbers in a list")

    x = int(input("Enter first range: "))
    y = int(input("Enter last range: "))

    list = []
    product = 1
    for a in range(x,y):
        user = int(input("Input Number: "))
        list.append(user)
    for b in list:
        product *= b
    print(product)

#Question 4
def reverse_print():

    print("Enter a string to print in reverse")

    a = input("Enter String: ")
    b = "" .join(reversed(a))
    print(b)

# Question 5
import math
def factorial():

    print("Enter a number/digit to get the factorial")
    
    a = int(input("Enter digit: "))
    b = 1
    for c in range(2, a + 1):
        b *= c
    print(b)

# Question 6
def num_in_range():

    print("Enter range and number to check if the number is in range")

    x = int(input("Enter first range: "))
    y = int(input("Enter second range: "))
    a = int(input("Enter number: "))

    if a in range(x, y):
        print("Yes! Number in range")
    else:
        print("No! Number not in range")

#Question 7
def upper_lower_case():

    print("Enter a sentence to check the number of upper and lower case characters")

    sentence = input("Enter Sentence: ")
    print("Lower case letters: ", sum(1 for a in sentence if a.islower()))
    
    print("Upper case letters: ", sum(1 for b in sentence if b.isupper()))

#Question 8
def unique_list():

    print("Enter different repeated numbers to print a unique list")

    x = int(input("Enter first range: "))
    y = int(input("Enter last range: "))

    l = []
    for a in range(x,y):
        user = int(input("Input Number: "))
        l.append(user)

    number = []
    for n in l:
        if n not in number:
            number.append(n)
    return number

#Question 9
def check_prime():

    print("Enter number to check if its a prime number or not")

    n = int(input("Enter digit: "))
    if (n == 1):
        return False
    elif (n == 2):
        return True
    for a in range(2, n//2):
        if n % a ==0:
            print("Not Prime")
    else:
        print("Prime")

def even_numbers():

    print("Enter numbers to print the list of even numbers")

    a = int(input("Enter first range: "))
    b = int(input("Enter last range: "))

    c = []
    for d in range(a, b):
        user = int(input("Input Number: "))
        c.append(user)
    even = []
    for x in c:
        if x % 2 == 0:
            even.append(x)
    print(even)