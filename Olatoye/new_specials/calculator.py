import operator


def ops_sign(operator_sign):
    ops = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv,
        "//": operator.floordiv,
        "%": operator.mod,
        "**": operator.pow
    }

    if sign in ops.keys():
        return ops[sign]


def calculator():
    num_1 = float(input("Enter number 1: "))
    operator_sign = input("Enter operator_sign: ")
    num_2 = float(input("Enter number 2: "))

    num = ops_sign(operator_sign)(num_1, num_2)
    print(f"Answer = {num}")

    counter = 2
    while True:
        sign = input("Enter sign or 'exit' to leave : ")
        if sign == "exit":
            print(f"\n\nFinal answer = {num}\nBye!")
            break
        else:
            counter += 1
            new_num = float(input(f"Enter number {counter}: "))
            num = ops_sign(operator_sign)(num, new_num)
            print(f"Answer = {num}")


calculator()
