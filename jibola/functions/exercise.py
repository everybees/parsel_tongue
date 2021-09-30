import math

# Question 1
# Write a Python function to find the Max of three numbers.
def max_three_number(a, b, c):
    return max(a, b, c)


# Question 2


# Question 3
# Write a Python function to multiply all the numbers in a list. Go to the editor
# Sample List : (8, 2, 3, -1, 7)
# Expected Output : -336
def multiply(list_):
   print(math.prod(list_))
    

# Question 4
# Write a Python program to reverse a string. Go to the editor
# Sample String : "1234abcd"
# Expected Output : "dcba4321"
def reverse_string(word):
    return word[::-1]


# Question 5
# Write a Python function to calculate the factorial of a number
# (a non-negative integer). 
# The function accepts the number as an argument.
def factorial(list):
    print(math.factorial(list))

# Question 6
# Write a Python function 
# to check whether a number falls in a given range.
def get_number_in_range(number,x,y):
    if number in range(x,y):
        print("%s the number is in range" %str(number))
    else:
        print("not in range.")


# Question 7
def upper_lower_case():
    pass

# Question 8
# Write a Python function that takes a list 
# and returns a new list with unique elements of the first list.

def unique_list(l):
    number = []
    for n in l:
        if n not in number:
            number.append(n)
    return number

# Question 9
# Write a Python function that takes a number as a parameter 
# and check the number is prime or not.

def check_prime( n):
    if(n==1):
        return False
    if (n==2):
        return True
    for a in range(2,n//2):
        if n%a==0:
            print("is not a prime number")
            break
    else:
         print("is a prime")

   

# Question 10
# Write a Python program to print 
# the even numbers from a given list.
def even_number(list_=[]):
    even_numbers = [str(number) for number in list_ if number % 2 == 0]
    print(", ".join(even_numbers))
    