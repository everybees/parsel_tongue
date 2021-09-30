
import operator

operation = {
"+": operator.add,
"-": operator.sub,
"*": operator.mul,
"/": operator.truediv,
"%": operator.mod,
"=": operator.eq
}
# while True:


first_input = float(input("Enter a number: "))
operator = input("Enter operator: ")
second_input = float(input("Enter another number: "))



if operator in operation.keys():
    answer = operation[operator](first_input, second_input)
print(answer)
while True:

 if["="] == operation:
        print("Calculating...")
        print(answer)
        break
operator = input("Enter operator: ")
another_number = float(input("Enter more numbers: "))
answer = operation[operator](answer, another_number)
print(answer)