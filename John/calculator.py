import operator
first_number = float (input("enter the first number "))
second_number = float (input("enter the second number "))
sign = input("enter the arithemetic sign")
ops = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv,  # use operator.div for Python 2
    '%' : operator.mod,
    '^' : operator.xor,
}
if sign in ops.keys():
       answer = ops[sign] (first_number , second_number)
       print( answer)
while True:
    sign = input("enter the arithemetic sign ")
    if sign == "exit" :
        print("the system is exiting...")
        print( answer)
        break
    third_number = float(input("enter the next value"))
    
    if sign in ops.keys():
        answer = ops[sign](answer, third_number )
        print( answer)
        
        
    



    