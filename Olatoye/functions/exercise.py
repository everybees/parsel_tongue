import math


# Question 1
def max_of_three_numbers():
    """
    Returns the maximum of three numbers
            Inputs:
                a (int): An integer
                b (int): An integer
                c (int): An integer
            Returns:
                maximum of the three user inputs
    """
    return max(int(input("Enter a: ")), int(input("Enter b: ")), int(input("Enter c: ")))


# Question 2
def sum_of_numbers():
    """
    Returns the sum of numbers in a list
            Input:
                list_: a list of integers separated by commas
            Returns:
                sum of the numbers in the user's list
    """
    list_ = [int(num) for num in input("Enter numbers separated by commas: ").split(",")]
    return f"Sum: {sum(list_)}"


# Question 3
def multiple_of_numbers():
    """
    Returns the multiple of numbers in a list
            Input:
                list_: a list of integers separated by commas
            Returns:
                multiplication of the numbers in the user's list
    """
    list_ = [int(num) for num in input("Enter numbers separated by commas: ").split(",")]
    return f"Multiplication: {math.prod(list_)}"


# Question 4
def reverse_string():
    """
    Returns the reverse of strings
            Input:
                word (string): a string entry
            Returns:
                reverse of user's string
    """
    return input("Enter your word: ")[::-1]


# Question 5
def factorial():
    """
    Returns the factorial of an integer
            Input:
                num (int): an integer entry
            Returns:
                factorial of user's input
    """
    return math.factorial(int(input("Enter your integer: ")))


# Question 6
def number_in_range():
    """
    Checks if a number is within a range of numbers
            Input:
                The integer entry to check, the lower limit of the range and the upper limit of the range
            Returns:
                True or False, depending on the position of the number within or without the range
    """
    return True if int(input("Enter the number: ")) in range(int(input("Enter lower limit: ")), int(input("Enter "
                                                                                                          "upper "
                                                                                                          "limit: "))
                                                             + 1) else False


# Question 7
def upper_and_lower():
    """
    Returns the number of uppercase and lowercase alphabets in a word
            Input:
                word of user's choice
            Returns:
                number of uppercase and lower alphabets
    """
    caps, lows = 0, 0
    for i in input("Enter your word: "):
        if i.islower():
            lows += 1
        else:
            caps += 1
    return f"Uppercase: {caps}", f"Lowercase: {lows}"


# Question 8
def unique_list_item():
    """
    Returns a list of unique numbers
            Input:
                list_: a list containing series of repeated entries
            Returns:
                unique_list: a sorted array of non-repetitive numbers
    """
    list_ = [int(num) for num in input("Enter numbers separated by commas: ").split(",")]
    unique_list = []
    for i in list_:
        if i not in unique_list:
            unique_list.append(i)
    return f"Sorted Unique list: {sorted(unique_list)}"


# Question 9
def prime_number():
    """
    Checks if a number is a prime number or not
            Input:
                num: an integer value
            Returns:
                True or False, depending on whether the number is a prime number or not
    """
    num = int(input("Enter integer: "))
    divisors = []
    for i in range(1, num):
        if num % i == 0:
            divisors.append(i)
    return f"{num} is a prime number" if len(divisors) == 1 or num == 1 else f"{num} is not a prime number"


# Question 10
def even_number_from():
    """
    Returns the even numbers in a list
            Input:
                list_: a list containing integers
            Returns:
                list of even numbers in list_
    """
    list_ = [int(num) for num in input("Enter numbers separated by commas: ").split(",")]
    return f"The even numbers are: {[num for num in list_ if num % 2 == 0]}"


# Question 11
def perfect_number():
    """
    Checks if a number is perfect or not
            Input:
                number: the integer entry to check
            Returns:
                True or False, depending on whether the number is a perfect number or not
    """
    number = int(input("Enter integer: "))
    divisors = [num for num in range(1, number) if number % num == 0]
    return f"{number} is a perfect number" if sum(divisors) == number else f"{number} is not a perfect number"


# Question 12
def palindrome():
    """
    Checks if a number is perfect or not
            Input:
                number: the integer entry to check
            Returns:
                True or False, depending on whether the number is a perfect number or not
    """
    word = input("Enter your word: ")
    return f"{word} is a palindrome" if word == word[::-1] else f"{word} is not a palindrome"


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
def hyphen_separator():
    """
    Returns the sorted arrangement of some words, separated by hyphen
            Input:
                words separated by hyphens
            Returns:
                sorted arrangement of some words
    """
    return "-".join(sorted(input("Enter the word").split("-")))


# Question 16
# def squared_numbers():
#     list_ = []
#     for i in range(1, 31):
#         if type(math.sqrt(i)) == "int":
#             list.append(i)
#         else:
#             pass
#     print(list_)

# Question 20
# def number_of_unique_local_variables(func_):
#     print(func_.__code__.co_nlocals)
