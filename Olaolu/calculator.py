import operator

operator = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
    "%": operator.mod,
    "=": operator.eq
}


first_input = float(input("Enter a number: "))
operator = input("Enter operator sign: ")
second_input = float(input("Enter another number: "))



if operator in operator.keys():
    answer = operator[operator](first_input, second_input)
print(answer)
while True:

    if["="] == operator:
        print(answer)
        break
operator = input("Enter operator: ")
another_number = float(input("Enter another numbers: "))
answer = operator[operator](answer, another_number)
print(answer)