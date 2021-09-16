import operator

# collect first number
# collect second number
# collect sign operator
# save answer
# collect sign operator in a loop
# collect the third numbers
# perfrom the math operation

ops = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
    "%": operator.mod,
    "^": operator.xor,
}
print("Enter first number")
first_number = float(input())
print("Enter the arithmetic sign")
sign = input()
print("Enter second number")
second_number = float(input())

if sign in ops.keys():
    answer = ops[sign](first_number, second_number)
    print(answer)

while True:
    print("Enter the arithmetic sign")
    sign = input()

    if sign == 'exit':
        print('stopped')
        print(total_answer)
        break

    print("Enter third number")
    third_number = float(input())

    if sign in ops.keys():
        total_answer = ops[sign](answer, third_number)
        print(total_answer)
