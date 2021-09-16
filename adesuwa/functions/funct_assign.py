# Question
import math


def max_of_three_numbers():
    firstnumber = int(input("Enter first number"))
    secondnumber = int(input("Enter second number"))
    thirdnumber = int(input("Enter third number"))

    print(max(firstnumber, secondnumber, thirdnumber))
def sum_of_list_numbers(odd = [2, 4, 6, 8]):
    #firstnumber = int(input())
    print(sum(odd))


def multiply_all_list_numbers(odd = [2, 4, 6, 8]):
    #firstnumber = int(input())
    print(math.prod(odd))

def reverse_a_string():
    inputstring = input("Enter something")
    print(inputstring[::-1])


def factorial_of_a_number(n):
    fact = 1

    for i in range(1, n + 1):
        fact = fact * i

    print("The factorial of", n,   "is : ", end="")
    print(fact)

def number_in_range(num):
    X = 1000
    Y = 7000
    #using comaparision operator
    if X <= num <= Y:
        print('The number {} is in range ({}, {})'.format(num, X, Y))
    else:
        print('The number {} is not in range ({}, {})'.format(num, X, Y))

def numbers_of_lower_and_uppercase(string):
    upper = 0
    lower = 0

    for i in range(len(string)):

        if 97 <= ord(string[i]) <= 122:
            lower += 1

    # For upper letters
        elif 65 <= ord(string[i]) <= 90:
            upper += 1

    print('Lower case characters = %s' % lower, 'Upper case characters = %s' % upper)

# number 8
def unique_element(list_):
    unique_list = []
    for numb in list_:
        if numb not in unique_list:
            unique_list.append(numb)
    result = f"sample list is {list_}, the unique list is: {unique_list}"
    print(result)


# number 9
def prime_number(number):
    number_divisors = []
    for numb in range(1, number):
        if number % numb == 0:
            number_divisors.append(numb)

    if len(number_divisors) == 1:
        print("number is a prime number")
    else:
        print("number is not a prime number")
    print(number_divisors)


# number 10
def even_number(list_):
    even_number_list = []
    for numb in list_:
        if numb % 2 == 0:
            even_number_list.append(numb)
    print(even_number_list)
    # print(numb if numb % 2 == 0 else "", end='')
    # even_number_list = [str(numb) for numb in list_ if numb % 2 == 0]
    # print("-".join(even_number_list))


# number 11
def perfect_number(number):
    perfect_number_list = []
    for numb in range(1, number):
        if number % numb == 0:
            perfect_number_list.append(numb)
    if sum(perfect_number_list) == number:
        print("Perfect number")
    else:
        print("number is not a perfect number")


# number 12
def string_palindrome(list_):
    print(True if list_ == list_[::-1] else False)


# number 14
def pangram(string):
    # strings = input("Enter words:  ")
    alphabet = ["abcdefghijklmnopqrstuvwxyz"]
    for i in alphabet:
        if i in string.lower().split():
            print("pass")
        else:
            print("fail")
            break


# number 15
def hyphen_separated_sequence(word):
    sequence = word.split('-')
    sequence.sort()
    print("-".join(sequence))