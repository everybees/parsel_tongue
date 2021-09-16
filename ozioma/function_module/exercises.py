def max_of_three_numbers():
    print('Enter three numbers in order to find their maximum.')
    a = int(input('Enter first number: '))
    b = int(input('Enter second number: '))
    c = int(input('Enter third number: '))

    if a > b:
        return a
    elif b > a and b > c:
        return b
    else:
        return c


def add_values():
    values = input('Enter integers separated by space: ').split()
    total = 0
    for value in values:
        total += int(value)
    return total


def sum_of_numbers_in_a_list():
    list_of_numbers = input('Enter integers separated by space: ').split()
    total = 0
    for number in list_of_numbers:
        total += int(number)
    return total


def multiply_numbers_in_a_list():
    numbers_in_a_list = input('Enter integers separated by space: ').split()
    total = 1
    for number in numbers_in_a_list:
        total *= int(number)
    return total


def reverse_a_string():
    string_input = input('Enter a string: ')
    reversed_string = string_input[::-1]
    return reversed_string


def factorial_of_a_number():
    input_value = int(input('Enter an integer: '))
    factorial = 1
    while input_value != 0:
        factorial *= input_value
        input_value -= 1
    return factorial


def check_number_within_a_range():
    desired_range = input('What is the desired range separated by space? ').split()
    answer_false = 'Not in range!'
    answer_true = 'In range!'
    number = int(input('What is the number? '))
    if number > int(desired_range[1]) or number < int(desired_range[0]):
        return answer_false
    else:
        return answer_true


def check_upper_and_lowercase_in_sentence():
    input_value = input('Enter string value here: ')
    count_small = 0
    count_big = 0

    for character in input_value:
        if character.islower():
            count_small += 1
        elif character.isupper():
            count_big += 1
    value = f'The no of small letters is {count_small}.' \
            f'\nThe no of big letters is {count_big}'
    return value


def create_a_list_with_unique_elements_of_given_list():
    given_list = input('Enter a list of numbers separated by space: ').split()
    list2 = []
    for element in given_list:
        list2 = [element for element in given_list
                 if given_list.count(element) < 2]
    return list2

# receive input
# if input is greater than 1, check if it is divisible by 2
# if yes, return not a prime number
# else if number is not divisible by 2, modulo with number
# if modulo operation gives 0, add the number to a list
    # if list length is greater than two, return false
    # else return true


def find_prime_number():
    user_number = int(input('Enter number: '))
    answer_true = 'Prime number'
    answer_false = 'Not prime number'
    value = 'invalid input'
    for number in range(2, (user_number+1)):

        if user_number > 1:

            if user_number % 2 == 0 or user_number == 9:
                return answer_false

            elif user_number % 2 != 0:
                list_of = [number for number in range(2, (user_number+1)) if user_number % number == 0]

                if len(list_of) > 2:
                    return answer_false
                else:
                    return answer_true


def print_even_number_from_a_list():
    input_value = input('Enter a list of numbers separated by space: ').split()
    return [int(even_number) for even_number in input_value if int(even_number) % 2 == 0]
