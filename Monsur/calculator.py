import operator

dictionary = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '%': operator.mod
}

first_number = float(input("Enter first number: "))
sign = input("Enter operator sign: ")
second_number = float(input("Enter second number: "))
if sign in dictionary.keys():
    answer = dictionary[sign](first_number, second_number)
    print(answer)
    while True:
        sign = input("Enter operator sign or 'exit' to end calculation: ")
        if sign == "exit":
            print(answer)
            break
        new_number = float(input("Enter another number: "))
        answer = dictionary[sign](answer, new_number)
        print(answer)

