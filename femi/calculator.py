import operator

ops= {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '%' : operator.mod,
    '/' : operator.truediv,
    '//' : operator.floordiv,
    '**' : operator.pow
}


first_number=int(input())

second_number= int(input())

sign=input()

if sign in ops:
    value= ops[sign](first_number, second_number)
    print(value)

while True:
    print(value)
    sign = input()
    if sign == "exit":
        print(value)
        break
    number = int(input())
    if sign in ops:
        value = ops[sign](value, number)
        print(value)
    if sign == "exit":
        print("exit...")
        break