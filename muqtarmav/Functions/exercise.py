# question 1
def max_of_three_numbers():
    print("Enter three numbers to find their their maximum")
    a = int(input("enter first number"))
    b = int(input("enter second number"))
    c = int(input("enter third number"))

    if a > b:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

# question 2
def sum_in_a_list():
    numbers = []
    total = 0
    for i in range(5):
        print("Enter value for number ", (i+1))
        digit = int(input())
        numbers.append(digit)
    for number in numbers:
        total += number
    return total


# question 3
def multiply_numbers_in_list():
    numbers_in_list = input("Enter numbers seperated by space: ").split()
    total = 1
    for values in numbers_in_list:
        total *= int(values)
    return total

# question 4
def string_reverse():
    string_input = input("Enter a string: ")
    reversed_string = string_input[::-1]
    return reversed_string

# question 5
def factorial_number():
    a = int(input("Enter a number: "))
    factorial = 1
    for i in range(1,a+1):
        factorial *= i
    return factorial


# question 6
def range_no():
    number = int(input("Enter a number:"))
    reply = "value is in range of 1-10"
    reply2 = "value is not in range"
    if number in range(2, 7):
        return reply
    else:
        return reply2

#question 7
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

# question 8
def unique_list():
    list = input("Enter a list of numbers seperated by space: ").split()
    list2 = []
    for a in list:
        list2 = [element for element in list
                 if list.count(element) < 2]
        return list2



# question 9
def test_prime():
    print("Enter number to check if its prime number or not")

    number = int(input("enter number"))
    if number == 1:
        return False
    elif number == 2:
        return True
    for x in range(2, number):
        if number % x == 0:
            print("not a prime number")
    else:
        print("its a prime number")

# #question 10
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