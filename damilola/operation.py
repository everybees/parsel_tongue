import operator

operators = {
    "+": operator.add,
    "-": operator.sub,
    "%": operator.mod,
    "*": operator.mul,
    "/": operator.truediv,
    "^":operator.xor
}
firstNumber = float(input("Enter first number: "))
secondNumber = float(input("Enter second number: "))
sign = input("Enter operator :")

if sign in operators.keys():
 answer = operators[sign](firstNumber,secondNumber)
print(answer)

      

while True:
    nextNumber = (input("Enter next number to continue or enter exit: "))
    if nextNumber== "exit":
        print("Exiting......")
        print(answer)
        break
    sign =input("Enter operator")
    if sign in operators.keys():
         answer = operators[sign](answer,(float)(nextNumber))
         print(answer)


         


    





