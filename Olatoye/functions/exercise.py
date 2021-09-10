# Question 1
def max_of_three_numbers(a, b, c):
    print(max(a, b, c))


# Question 2
def sum_of_numbers(list_):
    print(sum(list_))


def multiple_of_numbers(list):
    multiple = 1
    for i in list:
        multiple *= i
    print(multiple)


def reverse_string(word):
    print(word[::-1])