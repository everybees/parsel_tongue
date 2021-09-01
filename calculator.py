import operator

operation = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
    "%": operator.mod,
    "//": operator.floordiv,

}

first_input = float(input("Enter a number: "))
    operator = input("Enter operator")
    second_input = float(input("Enter another number: "))
    if operator in operation.keys():
        answer = operation[operator](first_input, second_input)
        print(answer)

        if


