#question1
from abc import abstractmethod
from operator import mul
from math import prod


def max_of_three_numbers():
 print("Enter three numbers")
 a=[]
 b = int(input())
 c = int(input())
 d = int(input())
 
 a.append(b)
 a.append(c)
 a.append(d)

 largest_number =a[0]

 for number in a:
    if number > largest_number:
       largest_number = number
 return largest_number

#question 2
def sum_all_numbers_in_a_list():
 abcd = []
 num = int(input("How many numbers"))
 for n in range(num):
     numbers = int(input("Enter number"))
     abcd.append(numbers)
 return(sum(abcd))

#question 3
def multiply_all_the_numbers_in_a_list():
 abcd =[]
 num = int(input("How many numbers"))
 for n in range(num):
     numbers = int(input("Enter number"))
     abcd.append(numbers)
 return (prod(abcd))

 #question 4
def reverse_a_string(str):
    word = " "
    for w in word:
        word = w + word
    return word 

#question 5
def even_number(l):

 number =[]
 for n in l :
     if n % 2 == 0:
      number.append(n)
 return n     

 #question 6
def unique_list(l):
    number = []
    for n in l:
        if n not in number:
            number.append(n)
    return number

def even_numbers(list):
 number = []
 for n in list:
     if n % 2 ==0:
         number.append(n)
         return n









 

    