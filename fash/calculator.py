import operator

signs = {
         '+': operator.add,
         '-': operator.sub,
         '*': operator.mul,
         '/': operator.truediv,
         '%':  operator.mod,
         '^': operator.xor
         }

first_number = float(input("Input your first number"))
second_number = float(input("Input your second number"))
sign = input("input your sign")


if sign in signs.keys():
    answer = signs[sign](first_number, second_number)
    print(answer)
    while True:

        sign = input("input your sign or exit to stop")
        if "exit" == sign:
            print("okay bye")
            break
        new_number =float(input("input the next number"))
        answer = signs[sign](answer, new_number)
        print(a9nswer)











