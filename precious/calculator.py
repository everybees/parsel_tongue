import operator

sign_operator = {
    "+": operator.add,
    "-": operator.sub,
    "/": operator.truediv,
    "*": operator.mul,
    "**": operator.pow,
    "%": operator.mod,
    "^": operator.xor,
}

answer = 0

number_1 = int(input("Enter first numbers: "))
sign = input("Enter operators: ")
number_2 = int(input("Enter second number: "))

if sign in sign_operator.keys():
    answer = sign_operator[sign](number_1, number_2)
    print("The total answer is : ", {answer})

# Play = True
while True:

    sign = input("Enter operators: ")
    if sign == 'exit':
        print("final answer is: ", answer)
        break

    elif sign in sign_operator.keys():
        number_3 = int(input("Enter number: "))
        answer = sign_operator[sign](answer, number_3)
        print("The total answer is : ", answer)

