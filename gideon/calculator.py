import operator

ops = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv,  # use operator.div for Python 2
    '%' : operator.mod,
    '^' : operator.xor,
}


first_number = float(input("Enter first number: "))
sign = input("Enter operator: ")
second_number = float(input("Enter second number: "))

# print(ops[sign] (first_number, second_number))

if sign in ops.keys():
    answer = ops[sign](first_number, second_number)
    print(answer)

while True:
    sign = input("Enter operator: ")
    if sign == "exit":
        print("Calculator exiting...")
        print(answer)
        break
    number = float(input("Enter next number: "))
    if sign in ops.keys():
        answer = ops[sign](answer, number)
        print(answer)