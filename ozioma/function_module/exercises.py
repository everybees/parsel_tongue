def max_of_three_numbers():
    a = int(input())
    b = int(input())
    c = int(input())

    if a > b:
        return a
    elif b > a and b > c:
        return b
    else:
        return c


def add_values():
    values = input().split()
    total = 0
    for value in values:
        total += int(value)
    return total
    pass


def define_list():
    numbers = []
    no_of_elements_in_list = int(input('How many elements are in your list? '))
    for number in range(no_of_elements_in_list):
        number = int(input('Type no: '))
        numbers.append(number)
    return numbers


def sum_of_numbers_in_a_list():
    list_of_numbers = input().split()
    total = 0
    for number in list_of_numbers:
        total += int(number)
    return total


def multiply_numbers_in_a_list():
    numbers_in_a_list = input().split()
    total = 1
    for number in numbers_in_a_list:
        total *= int(number)
    return total


def reverse_a_string():
    string_input = input()
    reversed_string = string_input[::-1]
    return reversed_string


def factorial_of_a_number():
    input_value = int(input())
    factorial = 1
    while input_value != 0:
        factorial *= input_value
        input_value -= 1
    return factorial
