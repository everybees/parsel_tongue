import operator
operators = {
    '+':  operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '%': operator.mod,
    '^': operator.pow,
}
def add(first_number, second_number): 
   return first_number + second_number

def sub(first_number, second_number):
    return first_number - second_number

def mul(first_number, second_number):
    return first_number * second_number

def truediv(first_number, second_number):
    return first_number / second_number

def mod(first_number, second_number):
    return first_number % second_number

def pow(first_number, second_number):
    return pow(first_number ^ second_number)  

print("Select operation.") 
print("1.Add") 
print("2.Subtraction") 
print("3.Multiplication")
print("4.True Division")
print("5.Modulus")
print("6.Power") 
choice = input("Enter your choice:")

first_number = int(input("Enter the first value:"))
second_number = int(input("Enter the second value:"))
 
if  choice == '1':
    print(first_number, "+", second_number, "=", add(first_number, second_number))
elif choice == '2':
     print(first_number, "-", second_number, "=", sub(first_number, second_number))
elif choice =='3':
    print(first_number, "*", second_number, "=", mul(first_number, second_number))

elif choice == '4':
    print(first_number, "/", second_number, "=", truediv(first_number, second_number))

elif choice =='5':
    print(first_number, "%", second_number, "=", mod(first_number, second_number)) 
elif choice == '6':
    print(first_number, "^", second_number, "=", pow(first_number, second_number))
else:
    print("Invalid input")           
 