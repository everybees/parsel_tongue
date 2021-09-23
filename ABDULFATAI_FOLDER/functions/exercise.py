
# #write a python function to find the max of three numbers.

def max_of_three_numbers(number1, number2, number3):
    number1 = int(input("Enter the first number"))
    number2 = int(input("Enter the second number"))
    number3 = int(input("Enter the third number"))

    max_number = number1
    if number2 > max_number:
        max_number = number2
    if number3 > max_number:
        max_number = number3    
    return max_number
print(max_of_three_numbers())    


# #write a python funtion to sum all the numbers in a list.
def sum(numbers):

    total = 0
    for j in numbers:
        total += j
    return total
my_list = []
number1 = int(input())
number2 = int(input())
number3 = int(input())
my_list = number1 + number2 + number3

print(sum(my_list))

#write a python function to multiply all the numbers in list(sample: 

def multiply_list(list) :
     
    total = 1
    for i in list:
         total = total * i
    return total
     
my_list = []
number1 = int(input())
number2 = int(input())
number3 = int(input())
my_list = number1 * number2 *number3
print(my_list) 
print(multiply_list(my_list))



#write a python program to reverse a string, (sample: "1234abcd")               

def reverse_string(string):
   f=""
   for i in string:
      f=i+f
   return f
string="1234abcd"
print(reverse_string(string))


#write a python function to calculate the factorial of a number
#(a non-negative integer). The function accepts the number as an argument

def factorial_of_number(number):
    number = int(input("Enter a number"))
    Counter = 0
    while number > 1:
        Counter += 1




def factorisation(n):
    fact = []
    i = 2
    while i<=n:     
       if n%i==0:      
        fact.append(i)
        n//= i
    else:
        i+=1
    return fact
#whether a number fall in a given range
def range():
    for i in range():



#write a python function that accepts a string and calculate the number
#of upper case letters and lower case letter.Sample: 'The quick brow fox'
def count_upper_case_letters(string):
    string = input("Enter a string:")
    count = 0
    for character in string:
        if character.isupper():    
            count += 1   
    return count
count = count_upper_case_letters('The quick Brow Fox')
print("The numbers of upper case letters is:", count)

def count_lower_case_letters(string):
    string = input("Enter a string:")
    Counter = 0
    for charater in string:
        if charater.islower():
            Counter += 1
    return Counter
Counter = count_lower_case_letters('The quick Brow Fox')
print("The numbers of lower case letters is:", Counter)


#even number
def even_number(list =[]):
    for n in list:
        if n % 2 == 0:
            print(n, " ")


####
def check_prime(n):
    if == 1:
    count = 2
    return False
    if n == 2:
        return True
    for a in range:    


