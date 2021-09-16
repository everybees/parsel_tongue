import operator

ops = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv,
    '%' : operator.mod,
    '^' : operator.pow,
}

first_number  = float(input())
second_number  = float(input())
sign = input()

if sign in ops:
    answer = ops[sign](first_number, second_number)
print(answer)


