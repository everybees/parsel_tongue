import math


# Question 1
def max_of_three_numbers(a, b, c):
    """
    Returns the sum of three numbers
            Parameter:
                    a (int): An integer
                    b (int): An integer
                    c (int): An integer
            Returns:
                    sum (int): sum of the three user inputs
    """
    print(max(a, b, c))


# Question 2
def sum_of_numbers(list_):
    """
    Returns the sum of numbers in a list
            Parameter:
                    list_: a list of integers
            Returns:
                    sum (int): sum of the numbers in the user's list
    """
    print(sum(list_))


# Question 3
def multiple_of_numbers(list_):
    print(math.prod(list_))


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


# Question 9
def prime_number(num):
    divisors = []
    for i in range(1, num):
        if num % i == 0:
            divisors.append(i)
    print(f"{num} is a Prime number" if len(divisors) == 1 or num == 1 else f"{num} is not a Prime number")


# Question 10
def even_number_from(list_):
    for i in list_:
        print(i if i % 2 == 0 else "", end=" ")


# Question 11
def perfect_number(number):
    divisors = []
    for i in range(1, number):
        if number % i == 0:
            divisors.append(i)
    print(f"{number} is a perfect number" if sum(divisors) == number else f"{number} is not a perfect number")


# Question 12
def palindrome(word):
    print(f"{word} is a palindrome" if word == word[::-1] else f"{word} is not a palindrome")


# Question 13
# def pascal_triangle


# Question 14
def pangram(sentence):
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    for i in alphabets:
        if i not in sentence:
            print("Not a pangram")
            break
        else:
            pass
    print("It is a pangram")


# Question 15
def hyphen_separator(word):
    print("-".join(sorted(word.split("-"))))


# Question 16
def squared_numbers():
    list_ = []
    for i in range(1, 31):
        if type(math.sqrt(i)) == "int":
            list.append(i)
        else:
            pass
    print(list_)


# Question 20
# def number_of_unique_local_variables(func_):
#     print(func_.__code__.co_nlocals)
