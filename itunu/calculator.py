import operator

ops = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv,
    '%' : operator.mod,
    '^' : operator.xor,
}

first_number  = float(input())
second_number  = float(input())
sign = input()

if sign in ops.key():
    answer = ops[sign](first_number, second_number)
print(answer)