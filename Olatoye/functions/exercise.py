# Question 1
import math


def max_of_three_numbers(a, b, c):
    print(max(a, b, c))


# Question 2
def sum_of_numbers(list_):
    print(sum(list_))


# Question 3
def multiple_of_numbers(list_):
    multiple = 1
    for i in list_:
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


# Question 7
def upper_and_lower(string_):
    caps, lows = 0, 0
    for i in string_:
        if i.islower():
            lows += 1
        else:
            caps += 1
    print(f"Uppercase: {caps}\nLowercase: {lows}")


# Question 8
def unique_list_item(list_):
    unique_list = []
    for i in list_:
        if i not in unique_list:
            unique_list.append(i)
    print(sorted(unique_list))
