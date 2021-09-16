#Question 1. Max of three numbers.
def max_of_three_numbers():  
    list = []
    num = int(input('How many numbers: '))
    for n in range(num):
        numbers = int(input('Enter number '))
        list.append(numbers)
    print("Maximum number is ", max(list), "\nMinimum number is ", min(list))


# Question 2. Sum all the numbers in a list
def lets_add_numbers():
    list = []  
    num = int(input('How many numbers: '))
    for n in range(num):
        numbers = int(input('Enter number '))
        list.append(numbers)
    print("The total ", sum(list))


# Question 3. Multiply all numbers in a list
import math
def multiplier():
    list = []
    num = int(input('How many numbers: '))
    for n in range(num):
        numbers = int(input('Enter number '))
        list.append(numbers)
    print("The product of the list is ",math.prod (list))


# Question 4. Reverse.
def textreverse():
    text = input("Enter a word and I'll print the reverse: ")
    print(text[::-1])


# Question 5. Factorial 
def factorial():
    num = int(input("Enter a number: "))    
    factorial = 1    
    if num < 0:    
        print(" A negative number, factorial doesn't exist")    
    elif num == 0:    
        print("The factorial of 0 = 1")    
    else:    
        for f in range(1,num + 1):    
            factorial = factorial*f    
    print("The factorial of",num,"is",factorial) 


# Question 6. Range
def number_bound():
    num_range = int(input("Enter range: "))
    n = int(input("Enter a number: "))
    if n in range(num_range):
        print("%s is in the range"%str(num_range))
    else :
        print("The number is outside the given range.")


# Questiion 7
def case_counter(): 
    word= input("Enter a word: ")
    casing={"UPPER_CASE":0, "LOWER_CASE":0}
    for letter in word:
        if letter.isupper():
            casing["UPPER_CASE"]+=1
        elif letter.islower():
            casing["LOWER_CASE"]+=1
        else:
            pass
        print ("Original String : ", word)
        print ("No. of Upper case characters : ", casing["UPPER_CASE"])
        print ("No. of Lower case Characters : ", casing["LOWER_CASE"])


# Question 8
def prime_number():
    number = int(input("Enter a number: "))
    if number % 1 == 0 and number % number == 0:
        print("prime")
    else:
        print("not prime")


# Question 9
def even_number_detector():
    number = []
    for elements in number:
        if elements % 2 == 0:
            number.append(elements)
            print("Number is an even number")
        else:
            print("Number is an odd number")

# Question 10
def prime_tester(n):
    if (n==1):
        print("false")
    elif (n==2):
        print("True")
    else:
        for elements in range(2,n):
            if(n % elements==0):
                print("False")
            else:
                print("True") 

     