import math


# Question 1
def max_of_three_numbers():
    print("This function calculates the max of three numbers\n")
    first_number = int(input("Enter the first Number\n"))
    second_number = int(input("Enter the second Number\n"))
    third_number = int(input("Enter the third Number\n"))
    maximum = max(first_number, second_number, third_number)
    print("The maximum between", first_number, ",", second_number, "and ", third_number, "is: ", maximum)


# Question 2

def sum_of_numbers_in_a_list():
    print("This function calculates the sum of a list\n")
    numbers = []
    num = int(input("how many numbers do you wanna add\n"))
    for n in range(num):
        number = int(input("Enter number"))
        numbers.append(number)
    sum_numbers = sum(numbers)
    print("The sum of the numbers is:", sum_numbers)


# Question 3
def product_of_numbers_in_a_list():
    print("This function calculates the product of numbers in a list")
    numbers = []
    num = int(input("how many numbers do you wanna multiply\n"))
    for n in range(num):
        number = int(input("Enter number"))
        numbers.append(number)
    product = math.prod(numbers)
    print("The product is:", product)


# Question 4

def reverse_a_string():
    print("This function calculates the reverse of a string\n")
    string_name = input("abeg write the word abi nah sentence way you wan reverse oooo\n")
    string_to_reverse = " "
    count = len(string_name)
    while count > 0:
        string_to_reverse += string_name[count - 1]
        count = count - 1
        print("The reverse string is: ", string_to_reverse)


# Question 5

def factorial_of_a_number():
    print("This function calculates the factorial of a number\n")
    number = int(input("abeg write the number way you wan find the factorial\n"))
    factorial = 1
    count = 1
    while count <= number:
        factorial = count * factorial
        count += 1
    print("The factorial of ", number, "is", factorial)


# Question 6
def check_whether_a_number_falls_in_a_given_range():
    print("This functions checks a number in a given set of numbers\n")
    number = int(input("Abeg write the number way you wan check if e dey for the range\n"))
    if 3 <= number <= 10:
        print("Number is in range")
    else:
        print("Number is not in the range")


# Question 7

def calculate_number_of_uppercase_and_lowercase_letters():
    print("This function displays the sum of the uppercase and lowercase letters in a word or sentence\n")
    string_word = input("Abeg write the word way get uppercase abi nah lowercase letters make we hellep you count am\n")
    upper_case = 0
    lower_case = 0
    for i in string_word:
        if i.isupper():
            upper_case += 1
        elif i.islower():
            lower_case += 1
    print("The number of uppercase letters are: ", upper_case)
    print("The number of lowercase letters are: ", lower_case)


# Question 8

def list_with_unique_element_of_the_first_list(list=[]):
    x = []
    for a in list:
        if a not in x:
            x.append(a)
    print(x)
   

# Question 9

def prime_numbers():
    print("This function calculates the prime number of a  number\n")
    counter = 2
    flag = False
    number = int(input("enter the number\n"))
    if number == 1:
        print("Number is not prime")
    else:
        while counter <= number / 2:
            if number % 2 == 0:
                flag = True
                break
            counter += 1
        if not flag:
            print("Number is prime")
        
        else:
            print("Number is not prime")


# Question 10

def write_out_the_even_numbers_in_a_list():
    numbers = [65, 78, 23, 12, 11, 90, 67, 90, 43, 4, 24, 54, 8]
    even_numbers = []
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
    print("The even numbers in the list are:", even_numbers)


def even_number(list=[]):
    print("This function displays the even numbers in a list of numbers\n")
    
    even_numbers = [str(number) for number in list if number % 2 == 0]
    print(" ,".join(even_numbers))
