import operator

def calculator():

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

def maximum_of_three_numbers():
    global result
    number_0ne = input("Enter first number:  ")
    number_two = input("Enter second number:  ")
    number_three = input("Enter third number: ")

    if number_three < number_0ne > number_two:
        result = number_0ne
    elif number_0ne < number_two > number_three:
        result = number_two
    elif number_0ne < number_three > number_two:
        result = number_three
    print({result})
