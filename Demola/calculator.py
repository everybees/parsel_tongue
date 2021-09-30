import operator

first_number = float(input("Enter first Number: "))
sign = input("Enter a Sign: ")
second_number = float(input("Enter Second Number: "))





operations = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
    '%': operator.mod,
}

if sign in operations.keys():
    answer = operations[sign](first_number, second_number)
    print(answer)
def calculate():
            while True:
                sign = input("Enter Operator: ")
            if sign == "exit":
                print("Calculator Exiting.......")
                print(answer)
                break

            number = float(input("Input Number: "))
            if sign in operations.keys():
                answer = operations[sign](answer, number)
                print(answer)