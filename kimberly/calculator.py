# import operator

# ops ={"+":operator.add,
#       "-":operator.sub,
#       "*":operator.mul,
#       "/":operator.truediv,
#       "%":operator.mod,
#       "^":operator.pow,
# }

# first_number=float(input("Enter first number: "))
# second_number=float(input("Enter second number: "))
# sign = input("Enter operator sign: ")
# if sign in ops:
#     answer = ops[sign](first_number,second_number)
#     print(answer) 
# while True:
#     sign = input("Enter operator sign or enter exit to break: ")
#     if "exit" == sign:
#         break
#     print(answer)
#     third_number = float(input("enter next : "))
    
# if sign in ops:
#     answer = ops[sign](answer, third_number)
#     print(answer) 
  
import operator

def calculate_something():
    ops={"+":operator.add,
          "-":operator.sub,
          "*":operator.mul,
          "/":operator.truediv,
          "%":operator.mod,
          "^":operator.pow
        }
    first_number = float(input("Enter the first number: "))
    second_number= float(input("Enter the second number: "))
    sign=input("Enter the operator sign: ")
    if sign in ops:
        answer= ops[sign](first_number,second_number)
        print(answer)
    while True:
        sign=input("Enter operator sign or enter exit to break: ")
        if "exit"==sign:
            print(answer)
            break
        else:
            third_number=float(input("Enter another number: "))
            if sign in ops:    
                answer=ops[sign](answer, third_number)
                print(answer)   
   
    
calculate_something()