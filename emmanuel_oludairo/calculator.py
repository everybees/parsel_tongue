import operator

ops = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,  # use operator.div for Python 2
    '%': operator.mod,
    '^': operator.xor,
}


def calculate():
    first_Number = float(input("Enter first number: "))
    sign = input("Enter operator: ")
    second_Number = float(input("Enter second number: "))
    if sign in ops.keys():
        answer = ops[sign](first_Number, second_Number)
        print(answer)
        while True:
            sign = input("Enter operator: ")
            if sign == "exit":
                print(answer)
                break
            number = float(input("Enter another number: "))
            if sign in ops.keys():
                answer = ops[sign](answer, number)
                print(answer)
