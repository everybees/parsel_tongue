# question
import random


def find_maximum_of_three_number():
    maximum = 0
    

    for a in range(0,3):
        user_input = int(input("enter the next number"))
        if user_input  > maximum:
            maximum = user_input 
    print("the maximum of the number is ",maximum)


# def find_maximum_of_three_number(a,b,c,):
#     if a > b and a > c:
#         return ("the largest number is " + a)
#     elif b > a and b > c:
#         return ("the largest number is " + b)
#     elif c > a and c > b:  
#         return ("the largest number is " + c)

# question 2
def sum_of_numbers(a=[]):
    total = 0
    for numbers in a:
        total += numbers
    print("the total of the sum is ", total)
#question 3
def find_multiplication(b=[0]):
    total = 1
    for couter in b:      
     total *= couter
     #return ("the sum of the number is",total)
    print("the  multiplication of the number is",total)
# question 4
def reverse(name):
  str = ""
  for i in name:
    str = i + str
  return print (str)
  

#question 5
def factorial_of_number(a =0 ) :
    factorial = 1
    for i in range(1,a + 1):
        factorial = factorial * i
    print("The factorial of", a, "is", factorial)
#question 6
def check_if_range(a):
    number = [1,2,3,4,5,6,7,8,9,10]
    if a in number:
        print("is in range")
    else:
 
        print("is not  in range")
        #another way to check in range.
    
#def test_range(n):
 #   if n in range(3,9):
  #      print( " %s is in the range"%str(n))
   # else :
    #    print("The number is outside the given range.")

# question 7
def calulate_nunmber_of_upper_case(userinput=""):
    upper_case = 0
    lower_case = 0
    for a in userinput:
        if a.isupper():
            upper_case += 1
        elif a.islower():
            lower_case +=1
        else:
            pass
    print("the original string is", userinput)
    print("the number of upper case is ", upper_case,"the number of lower case is ",lower_case)


    def upa(user=""):
        upcas = 0
        locas =0
        for a in userinput:
            if a.isupper():
                upacs +=1
            elif a.islower():
               locas +=1
            else:
                continue
            print()
            print()
                


# question 8
def return_unique_number(userinput):
    uniquelist = []
    for a in userinput:
     if a not in uniquelist:
      uniquelist.append(a)
    print ("the unique list is ", uniquelist) 
#question 9
def test_prime(n):
    if (n==1):
        return False
    elif (n==2):
        return True
    else:
        for x in range(2,n):
            
            
            if(n % x==0):

                print("is not a prime number")
                break
            else:
               print("is a prime ")         
#def collect_user_details():
def collect_user_details():
    students = int (input("how many students do u have"))
    
    dictionary_user = {}
    
    for i in range(students):
        first_name = input("enter your first name")
        last_name = input("enter your last name")
        email_address = input("enter your email address")
        password = input("enter your password")
        dictionary_user["user" + str(i+1)] = {"first_Name": first_name, "lastname":last_name, "email":email_address, "Password":password}
    print(dictionary_user)
# def collect_user_details():
#     marks = {}
#     for i in range(10):
#         student_name = input("Enter student's name: ")
#         student_mark = input("Enter student's mark: ")
#         marks [student_name.title()] = student_mark
#     print(marks)
# def collect_user_details():
#     marks = {}

#     for i in range(2):
#         student_name = input("Enter student's name: ")
#         student_mark = input("Enter student's mark: ")


#         marks = {student_name.title():student_mark}

#     print(marks)

      


