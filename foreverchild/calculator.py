import operator

print("Enter values to calculate")
ops = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv,
    '%' : operator.mod,
    '^' : operator.xor,
    }

def calculate():
    while True:
        first_number = float(input())
        sign = input()
        second_number = float(input())
        if sign in ops.keys():
            answer = ops[sign](first_number,second_number)
            print(answer)
            third_number = float(input())
            sign = input()
            fourth_number = float(input())
            second_answer = ops[sign](third_number,fourth_number)
            print(second_answer)
            final_answer = (answer + second_answer)
            print(final_answer)
            
    # sign = input()
    # third_number = float(input())
    # sign = input()
    # fourth_number = float(input())
    
  
        


fourth_number = float(input())
fifth_number = float(input())
sign = input()
