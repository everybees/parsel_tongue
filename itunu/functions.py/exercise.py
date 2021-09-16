# Question 1
def max_of_three_numbers(a, b, c):
  a = int(input())
  b = int(input())
  c = int(input())
  numbers = [a, b, c] 
  print(max(numbers))


# Question 2
def sum_of_numbers_in_a_list():   
  list = []
  number = int(input('How many numbers: '))
  for n in range(number):
    numbers = int(input('Enter number '))
    list.append(numbers)
  print("Sum of numbers in given list is :", sum(list))


#  Question 3
# def multiple_of_numbers_in_a_list():
#   list = []
#   number = int(input('How many numbers: '))
#   for n in range(number):
#     numbers = int(input('Enter number '))
#     list.append(numbers)
#   print("Sum of numbers in given list is :", math.prod(list))
#   or
def multiple_of_numbers_in_a_list(list):
  print("Sum of numbers in given list is :", math.prod(list))

#  Question 4
#  def reverse_a_string():
#  string = input("Enter a string: ")
#  string = string.lower()
#   print(string[::-1])
  string = input('Tell me a word of your choice: ')
  last = len(ast)
  for i in range(last): 
      print(last-1-i)
  for i in range(last):
      print(string[last-1-i])
  rast = ""
  for i in range(last):
      rast += string[last-1-i]
  print(rast)

#  Question 5

def factorial_of_a_number():
    number = int(input("enter the number you want to find the factorial\n"))
    count = 1
    factorial = 1
    while count <= number:
        factorial = count * factorial
        count += 1
    print("The factorial of ", number, "is ", factorial)


# Question 6
def check_whether_a_number_falls_in_a_given_range():
    number = int(input("enter a number\n"))
    if number in range(3,9):
        print( number, " is in the range", str(number))
    else :
        print("The number is outside the given range.")

# Question 7
def calculate_number_of_upper_case_letters_and_lower_case_letters():
    string=input("Enter string:")
    count1=0
    count2=0
    for i in string:
        if(i.islower()):
            count1=count1+1
        elif(i.isupper()):
            count2=count2+1
    print("The number of lowercase characters is:")
    print(count1)
    print("The number of uppercase characters is:")
    print(count2)
    
# Question 8

# Question 10
def even_number(list):
    for n in list:
        if n % 2 == 0:
            print(n)