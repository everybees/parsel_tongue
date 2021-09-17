# Question 1: write a python functions to find the maximum of three numbers;
import math


def max_of_three_numbers(a, b, c):
    print(max(a, b, c))
    # a = int(input())
    # b = int(input())
    # c = int(input())
    #
    # if a > b and a > c:
    #     print(a)
    # elif b > c and b > a:
    #     print(b)
    # else:
    #     print(c)


def sum_of_numbers_in_a_list(add=[2, 4, 89, 4]):
    print(sum(add))


def multiply_all_list_numbers(set):
    print(math.prod(set))


def factorial_of_number(n):
    fact = 1
    for num in range(2, n + 1):
        fact *= num
    print(fact)


# print(math.factorial(n))

def number_in_range(num):
    x = 1000
    y = 5000
    if x <= num <= y:
        print("The number {} is in range ({}, {})".format(num, x, y))
    else:
        print("The number {} is not in range ({}, {})".format(num, x, y))


def numbers_of_lower_and_uppercase(string):
    lowercase_letter_count = 0
    uppercase_letter_count = 0

    for letter in string:
        if letter.isupper():
            uppercase_letter_count += 1
        elif letter.islower():
            lowercase_letter_count += 1

    print("The uppercase numbers are-", uppercase_letter_count, " : ", "The lowercase number are-",
          lowercase_letter_count)


def reverse_a_string():
    text = "shem"[::-1]
    print(text)


def unique_element_list(num):
    unique = []
    for item in num:
        if item not in unique:
            unique.append(item)
    print(unique)


def prime_number(n):
    # prime_number = [str(prime) for prime in list_ if number % 2 == 0 and number % 2 == 1]
    # print(" ".join(prime_number))
    # if (n == 1):
    #     return  False
    # if (n == 2):
    #     return True
    # for a in range(2, n // 2):
    #     if n % a == 0:
    #         print("is not a prime number")
    #         break
    # else:
    #      print("Is a prime")
    #
    number = int(input())
    for x in range(2, number // 2):
        if number % x == 0:
            print("is not a prime number")
            break
    else:
        print("Is a prime")


def even_number(list_={}):
    even_number = [str(number) for number in list_ if number % 2 == 0]
    print(", ".join(even_number))
