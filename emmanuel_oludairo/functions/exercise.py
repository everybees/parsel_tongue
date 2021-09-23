# Question 1
def max_of_three_number():
    print("Check for the maximum number")
    print("Enter any 3 numbers: ")
    number1 = int(input())
    number2 = int(input())
    number3 = int(input())
    # if a > b and a > c:
    #     return a
    # elif b > a and b > c:
    #     return b
    # elif c > a and c > b:
    print("max =", max(number1, number2, number3))


# Question 2
def sum_of_numbers_in_a_list():
    print("Sum of a list")
    x = input("Enter a list elements seperated by space: ")
    number = x.split()
    sum = 0
    for element in number:
        sum += int(element)
    print("sum =", sum)


# Question3
def product_of_numbers_in_a_list():
    print("Multiplication")
    x = input("Enter a list element seperated by space: ")
    number = x.split()
    product = 1
    for element in number:
        product *= int(element)
    print("product =", product)
    # return product


# Question4
def reverse_a_string():
    print("Reverse checking")
    print("Enter a string: ")
    x = input()
    text = x[::-1]
    print(text)


# Question5
def factorial_of_a_number():
    print("Factorial checking")
    print("Enter a number less of equal to 5: ")
    n = int(input())
    # factorial = 1
    # for i in range(1, num + 1):
    #     factorial = factorial * i
    factorial = n * (n - 1) * (n - 2) * (n - 3)
    print("The factorial of", n, "is", factorial)


# Question6
def number_in_a_range():
    print("Check if number is a range")
    print("Enter any number between 1 and 100: ")
    i = int(input())
    if i in range(1, 100):
        print("number is in range")
    else:
        print("number not in range")


# Question7
def number_of_upper_and_lower_case():
    print("Check for the lower and upper case")
    print("Type: 'The quick Brown Fox'")
    string = input()
    lowercase_letter_count = 0
    uppercase_letter_count = 0
    for letter in string:
        if letter.isupper():
            uppercase_letter_count += 1
        elif letter.islower():
            lowercase_letter_count += 1
    print("Upper case count: ", uppercase_letter_count, "Lower case count: ", lowercase_letter_count)


# Question8
def unique_element_list():
    print("unique number sorting")
    x = input("Enter a list elements seperated by space: ")
    number = x.split()
    # number = (2, 1, 4, 2, 4, 5, 1, 7, 7)
    unique = []
    for element in number:
        if element not in unique:
            unique.append(element)
    print(unique)


# Question 9
def check_if_a_number_is_a_prime_number():
    print("Prime number checking")
    print("Enter any number to check")
    number = int(input())
    for x in range(2, number // 2):
        if number % x == 0:
            print("number is not a prime number")
            break
    else:
        print("number is a prime number")
