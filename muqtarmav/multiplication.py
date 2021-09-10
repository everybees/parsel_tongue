
import operator

ops = {
    "+": operator.add,
    "-": operator.sub,
    "/": operator.truediv,
    "*": operator.mul,
    "^": operator.pow,
    "%": operator.mod,
    "**": operator.pow


}

first_number = float(input("Enter first number "))
while True:
    second_number = float(input("Enter second number "))
    signs = input("Enter signs ")

    if signs in ops.keys():
        answer = ops[signs](first_number, second_number)
        print(answer)




    
    if signs == "exit":
        print("Existing...")
        break
    # if signs in ops.keys():
    #     answer = ops[signs](first_number, second_number)
    #     print(answer)
