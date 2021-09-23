import operator

def calculation():
    allowed_operators = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv}
    
    total = 0
    print("Enter 0 as first digit and 0 as second digit and any operator "
          "when you are ready to exit the program")
    print()
    while True:
        first_number = int(input("Enter the first digit\n"))
        second_number = int(input("Enter the second digit\n"))
        string_operator = input("Enter the operator sign\n")
        if string_operator in allowed_operators:
            result = allowed_operators[string_operator](first_number, second_number)
            print("The result is ", result)
            total = total + result
            if first_number == 0 and second_number == 0:
                break
    print("The grand total is ", total)
