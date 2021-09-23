# Quetsion 1

def max_of_three_numbers(a, b, c):       
    return max(a, b, c)


#Quetsion 2

def sum_of_number_in_a_list(list):
    total = 0
    for i in list:
        total += i
    print (total)

# Question 3
def multiply_numbers():
    import math
    numbers = [3, 6, 7]
    result = math.prod(numbers)
    print(result)


# # Question 4
def reverse_a_string(words):
    return words[::-1]


# Question 5
def calculate_factorial():
    number = int(input("Enter a number: "))
    factorial = 1
    for num in range(1, number+1):
        factorial *= num
    return factorial


# Question 6
def check_range(): 
    a = int(input("Enter a number: "))
    if a in range(1, 20):
        print("number is in range")
    else: 
        print("number is not in range")

# Question 7
def test_for_case(s):
    d = {"UPPER_CASE": 0, "LOWER_CASE": 0}
    for i in s:
        if i.isupper():
            d["UPPER_CASE"]+=1
        elif c.islower():
            d["LOWER_CASE"]+=1
        else:
            pass
        print("Original string: ",s)
        print("Number of upper case characters: ", d["UPPER_CASE"])
        print("Number of lower case characters: ", d["LOWER_CASE"])

# Question 8
# def unique_list(list):
#     for number in list:

# Question 9
def prime_number(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2,n):
            if n % i == 0:
                return False
            return True

# Question 10
def even_number(list_):
    for i in list_:
        if i % 2 == 0:
            print(i)
    # even_numbers = [str(number) for number in list_ if number % 2 == 0] 
    # print(" ".join(even_numbers))