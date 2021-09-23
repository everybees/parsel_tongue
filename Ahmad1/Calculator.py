import operator
operators = {
    '+' : operator.add,
    '-' : operator.sub,
    '/' : operator.truediv,
    '*' : operator.mul,
    '%' : operator.mod,
    '^' : operator.xor,
    '**': operator.pow,
    '//': operator.floordiv
}
first_number = int(input("Enter number: "))
sign = input("Enter operator: ")
answer = 0
second_number = int(input("Enter number"))
if sign in operators.keys():
    answer = operators[sign](first_number, second_number)
    print(answer)
while True:
    sign = input("Enter operator: ")
    if sign == 'exit':
        print(answer)
        break
    number = int(input("Enter number: "))
    if sign in operators.keys():
        answer = operators[sign](answer,number)
        print(answer)