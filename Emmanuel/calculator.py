import operator

ops = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '%': operator.mod,
    '^': operator.xor,
}

    
first_number = int(input("Enter first number: "))
sign = input("enter sign: ")
second_number = int(input('enter another number: '))
if sign in ops:
    answer = ops[sign](first_number, second_number)
    print(answer)


while True:
    
    sign = input("enter operator sign: ")
   

    if sign == 'exit':
        print("Exiting...")
        print(answer)
        break
    if sign in ops.keys():
         number = int(input("enter another number: "))
         answer = ops[sign](answer, number)
         print(answer)
    
