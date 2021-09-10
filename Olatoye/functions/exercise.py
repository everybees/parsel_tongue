# Question 1
import math


def max_of_three_numbers(a, b, c):
    print(max(a, b, c))


# Question 2
def sum_of_numbers(list_):
    print(sum(list_))


# Question 3
def multiple_of_numbers(list):
    multiple = 1
    for i in list:
        multiple *= i
    print(multiple)


# Question 4
def reverse_string(word):
    print(word[::-1])


# Question 5
def factorial(num):
    print(math.factorial(num))


# Question 6
def number_in_range(num, lower_lim, upper_lim):
    print(True if num in range(lower_lim, upper_lim + 1) else False)


