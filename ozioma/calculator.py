import operator

operator_signs = {"+": operator.add,
                  "-": operator.sub,
                  "*": operator.mul,
                  "//": operator.floordiv,
                  "/": operator.truediv,
                  "**": operator.pow
                  }

while True:
    first_number = float(input())
    second_number = float(input())
    sign_operator = input()
    for sign in operator_signs:
        final_value = operator_signs[sign](first_number, second_number)
        if sign_operator != "exit":
            if sign_operator == sign:
                print(final_value)
        else:
            print(final_value)
            break

















# to simulate a real calculator
# if user enter first number, it displays
#
#
#
#
