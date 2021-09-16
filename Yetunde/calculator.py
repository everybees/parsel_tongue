import operator

ops = {"+": operator.add, 
        "-": operator.sub, 
        "/": operator.truediv, 
        "*": operator.mul,
        "^": operator.xor,
        "%": operator.mod}


def calculator():  
    first_number = int(input("Enter a number: "))
    signs = input("Enter a sign: ")
    second_number = int(input("Enter a number: "))
    
    if signs in ops.keys():
        answer = ops[signs](first_number, second_number)
        print (answer)

    while True:
        signs = input("Enter a sign: ")   
        if signs == 'exit':
            print (answer)
            break
        number = int(input("Enter a number: "))

        if signs in ops.keys():
            answer = ops[signs](answer, number)
            print (answer)


