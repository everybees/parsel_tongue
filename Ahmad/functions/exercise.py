# Question 1
def max_of_three_numbers():
    print("Enter values to be compared:")
    a = []
    b = int(input("enter first number:"))
    c = int(input("enter second number:"))
    d = int(input("enter third number:"))
    a.append(b)
    a.append(c)
    a.append(d)
    largest_number = a[0]
    for value in a:
        if value > largest_number:
            largest_number = value
    print("Largest number is: ")
    return largest_number


def sum_of_numbers_in_a_list(b=[]):
    total = 0
    for values in b:
        total = total + values
    print("sum of the numbers in the list is: ")
    return total


def multiply_numbers_in_a_list(b=[]):
    total = 1
    for values in b:
        total = total * values
    print("Product of values in list is: ")
    return total


def reverse():
    word = input("Enter word to be printed in reverse: ")
    new_word = ''
    length = len(word) - 1
    while length >= 0:
        new_word += word[length]
        length -= 1
    return new_word


def factorial(number):
    value = int(number)
    fac = 1
    while value > 0:
        fac = fac * value
        value -= 1
    print("Factorial is: ")
    return fac


def range_checker(number):
    a = []
    value = int(number)
    for x in range(100):
        a.append(x)
    if value in a:
        print("Number supplied is in range")
    else:
        print("Number supplied is out of range")


# Question 7
def case_calculator(text):
    upper_case = 0
    lower_case = 0
    for letter in text:
        if letter.isupper():
            upper_case += 1
        else:
            lower_case += 1
    print("Number of lower case letters present is: ", lower_case)
    print("Number of upper case letters present is: ", upper_case)


# Question 8
def unique_elements(b=[]):
    c = []
    for x in b:
        if x not in c:
            c.append(x)
    return c


# Question 9
def prime_number():
    a = int(input("Enter a number: "))
    first_response = "is a prime number"
    second_response = "is not a prime number"
    factors = 0
    for number in range(2, a + 1):
        if a % number == 0:
            factors += number
        if factors == a:
            print(a, end=" ")
            return first_response
        else:
            print(a, end=" ")
            return second_response


# Question 10
def even_number_in_list(b=[]):
    c = []
    for i in b:
        if i % 2 == 0:
            c.append(i)
    return c











