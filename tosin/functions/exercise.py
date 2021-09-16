#Question 1
def max_of_three_numbers():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    c = int(input("Enter last number: "))
    maximum = a
    if b > maximum:
        maximum = b
    if c > maximum:
        maximum = c
    return maximum


#Question 2
def sum_of_numbers_in_a_list():
    numbers = []
    total = 0
    for i in range(5):
        print("Enter value for number ", (i+1))
        digit = int(input())
        numbers.append(digit)
    for number in numbers:
        total += number
    return total

#Question 3
def multiply_numbers_in_list():
    numbers = []
    total = 0
    for i in range(5):
        print("Enter value for number ", (i+1))
        digit = int(input())
        numbers.append(digit)
    total = 1
    for number in numbers:
        total *= number
    return total

#Question 4
def reverse_string():
    texts = input("Enter a word: ")
    new_word = ''
    length = len(texts) - 1
    while length >= 0:
        new_word += texts[length]
        length -= 1

    return new_word

#Question 5
def calculateFactorial():
    a = int(input("Enter a number: "))
    factorial = 1
    for i in range(1,a+1,):
        factorial *= i
    return factorial

#Question 6
def find_range():
    a = int(input("Enter a number: "))
    response = "The value is in range of 1-10"
    second_response = "number is not in range"
    if a in range(1,21):
        return response    
    else:
        return second_response

#Question 7
def count_lower_and_uppercase():
    words = input("Enter a sentence: ")
    letters = {'upper_case': 0, 'lower_case': 0}
    for letter in words:
        if letter.islower():
            letters["lower_case"]+=1
        if letter.isupper():
            letters["upper_case"]+=1
    print("The number of uppercase is: ", letters["upper_case"])
    print("The number of lowercase is: ", letters['lower_case'])

#Question 8
def unique_list():
    print("Enter 10 numbers at random with no regards for uniqueness")
    list = []
    for i in range(10):
        number = int(input("Enter a number: "))
        list.append(number)
    new_list = []
    for number in list:
        if number not in new_list:
            new_list.append(number)
    return new_list

#Question 9
def prime_number():
    a = int(input("Enter a number: "))
    first_response = "is a prime number"
    second_response = "is not a prime number"
    factors = 0
    for number in range(2, a+1):
        if a % number == 0:
            factors += number

    if factors == a:
        print(a, end=" ")
        return first_response
    else:
        print(a, end=" ")
        return second_response

#Question 10
def even_number_in_list():
    print("A list of 10 numbers")
    list = []
    for i in range(10):
        digit = int(input("Enter a number: "))
        list.append(digit)
    x = []
    for number in list:
        if number % 2 == 0:
            x.append(number)
    return x
