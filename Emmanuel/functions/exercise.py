import math
# Question 1

def max_of_three_numbers():
    first_number = int(input())
    second_number = int(input())
    third_number = int(input())
    return max(first_number,second_number,third_number)

    # Question 2     
def sum_of_a_list():
    lists = []
    number= int(input("Enter how many numbers you wish to be summed:"))
    for i in range(number):
        numbers = int(input())
        lists.append(numbers)
    b = sum(numbers)
    print(b)


    # Question 3

def multiply_numbers_in_a_list():
    number = []
    numb = int(input("how many numbers do you want to multiply"))
    for item in range(numb):
        numbers = int(input("enter numbers\n"))
        number.append(numbers)
        product = math.prod(numbers)
    print(product)

#     # Question 4
def reverse_string(x):
    return x[::-1]
    
#     # Question 5

def factorial():
    number =int(input("Enter number"))     
    if number < 0:
        print("Sorry, factorial does not exist for negative numbers")
    elif number == 0:
       print("The factorial of 0 is 1")
    else:
     return(math.factorial(number))

#     # Question 6

def number_fall_in_a_given_range(na):
    n = range(11-20)
    if na < n:
        print("Number not within the range")
    elif na > n:
        print("Number is out of range")
    else:
        print("Number is within the range")

# Question 7
def string_counter():
    str=input("Enter strings: ")
    upper=0
    lower=0
    for i in range(len(str)):
      if(str[i]>='a' and str[i]<='z'):
          lower+=1
      elif(str[i]>='A' and str[i]<='Z'):
          upper+=1
    print('Lower case letters= ',lower)
    print('Upper case letters=' ,upper)

# Question 8
def list_unique_elements(list=[]):
    elements =[]
    for m in list:
        if m not in elements:
            elements.append(m)
    return elements