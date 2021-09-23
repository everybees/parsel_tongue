import math

# number1
import operator


def maximum_of_three_numbers():
    print("get the maximum number of three numbers")
    print(max(int(input("enter 1st numb: ")), int(input("enter 2nd numb: ")), int(input("enter 3rd numb: "))))


# number2
def sum_number(list_):
    sum_total = 0
    for numb in list_:
        sum_total += numb
        print(numb)


# number3
def multiple(list_):
    print(math.prod(list_))


# number4
def reverse_a_string(name):
    print(name[::-1])


# number5
def factorial(number):
    print(math.factorial(number))


# number 6
def number_fall(num, lower_bound, upper_bound):
    for numb in range(lower_bound, upper_bound):
        if num == numb:
            print(True)


# number 7
def string_uppercase_lowercase():
    global c
    name = input("Enter name:  ")

    d = {"UPPER_CASE": 0, "LOWER_CASE": 0}
    for c in name:
        if c.isupper():
            d["UPPER_CASE"] += 1
        elif c.islower():
            d["LOWER_CASE"] += 1
    print("the original input is: ", c, "\n", "the number of upper case is: ", d["UPPER_CASE"], "\n",
          "the number of lower case is: ", d["LOWER_CASE"])


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


# number 16
def value_square_numbers():
    number = []
    for i in range(1, 31):
        if type(int(math.sqrt(i))) == type(1):
            number.append(i ** 2)
    print(number)


# number 17
def function_decorators():
    user = input("Enter name: ")
=======
import math

# number1
import operator


def maximum_of_three_numbers():
    print("get the maximum number of three numbers")
    print(max(int(input("enter 1st numb: ")), int(input("enter 2nd numb: ")), int(input("enter 3rd numb: "))))


# number2
def sum_number(list_):
    sum_total = 0
    for numb in list_:
        sum_total += numb
        print(numb)


# number3
def multiple(list_):
    print(math.prod(list_))


# number4
def reverse_a_string(name):
    print(name[::-1])


# number5
def factorial(number):
    print(math.factorial(number))


# number 6
def number_fall(num, lower_bound, upper_bound):
    for numb in range(lower_bound, upper_bound):
        if num == numb:
            print(True)


# number 7
def string_uppercase_lowercase():
    global c
    name = input("Enter name:  ")

    d = {"UPPER_CASE": 0, "LOWER_CASE": 0}
    for c in name:
        if c.isupper():
            d["UPPER_CASE"] += 1
        elif c.islower():
            d["LOWER_CASE"] += 1
    print("the original input is: ", c, "\n", "the number of upper case is: ", d["UPPER_CASE"], "\n",
          "the number of lower case is: ", d["LOWER_CASE"])


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


# number 16
def value_square_numbers():
    number = []
    for i in range(1, 31):
        if type(math.sqrt(i)) == type(1):
            number.append(i)
            print(number)
