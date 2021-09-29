import math 
# Question 1
import math
def max_of_three_numbers():
    a= int(input("Enter first number: "))
    b= int(input("Enter second number: "))
    c= int(input("Enter third number: "))
    print(max(a,b,c))

# Question 2
def sum_of_numbers_in_a_list():
    a=int(input("Enter first range: "))
    b=int(input("Enter second range: "))
    list = []
    sum=0
    for c in range(a,b):
        d = int(input("Enter number: "))
        list.append(d)
    for e in list:
        sum += e
    print(sum)

# Question 3

def multiply_numbers_in_a_list():
    a=int(input("Enter first range: "))
    b=int(input("Enter second range: "))
    list=[]
    product =1
    for c in range(a,b):
        d = int(input("Enter number: "))
        list.append(d)
    for e in list:
        product *= e
    print(product)         

# Question 4
def reverse_string():
    s=(input("Enter string: "))
    string = " ".join(reversed(s))
    print(string)

# Question 5
import math

def calculate_factorial_of_a_number():
    a=int(input("Enter a number: "))
    result=math.factorial(a)
    print(result)

# Question 6
def find_number_in_range():
    a=int(input("Enter first range"))
    b=int(input("Enter second range"))
    c=int(input("Enter the number"))

    if c in range(1,10):
        print("number is in range") 
    else: 
        print("number is not in range")    

# Question 7
def calculate_case_of_letter():
    sentence=input("Enter a string: ")
    print("upper_case: ", sum(1 for a in sentence if a.isupper()))
    print("lower case: ", sum(1 for b in sentence if b.islower())) 

# Question 8
def unique_list(_list=[]):
    new_list =[]
    a=int(input("Enter first range: "))
    b=int(input("Enter second range: "))
    list=[]
    
    for c in range(a,b):
        d=int(input("Enter a number: "))
        list.append(d)
    number = []
    for e in list:
        if e not in number:
            number.append(e)
    print(number)

    # Question 9   
def check_ifprime():
    a=int(input("Enter any number: "))   
    if (a==1):
        return False
    elif (a==2):
        return True
    else:
        for x in range(2,a):
            if(a % x==0):
                return False
        else:    
                return True    

    #Question 10
def is_even_list():
    a=int(input("Enter first range: "))   
    b=int(input("Enter second range: "))
    list=[]   
    for c in range(a,b):
        d=int(input("Enter number: "))
        list.append(d)
    new_list=[]    
    for n in list:
        if n%2==0:
            new_list.append(n)
    print(new_list)
                



             





    

    




