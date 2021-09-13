import operator

ops = {"+": operator.add,
         "-": operator.sub,
         "/": operator.truediv,
         "*": operator.mul,
         "%": operator.mod,
         "^": operator.xor
 }

first_number = float(input("Enter the first  "))
second_number = float(input("Enter the second number "))

sign = input()
if sign in ops.keys():
        answer = ops[sign](first_number, second_number)
        print(answer)

while True:

    sign = input("enter an operator ")
    
    if sign == "exit":
        print("exiting")
        print(answer)
        break

    third_number = float(input("Enter another number "))
    if sign in ops.keys():
        answer = ops[sign](answer, third_number)
        print(answer)

    
    