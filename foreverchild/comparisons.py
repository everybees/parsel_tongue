print("Foreverchild")
# solution using none casting method
promt = input("Enter a Number")
number_one = input(" ")
promt = input("Enter a second number")
second_number = input(" ")
prompt = input("Enter third Number")
third_number = input(" ")

compare = print(number_one < second_number and second_number< third_number)

# solution using casted methed

first_number = int(input())
second_number = int(input())
if first_number < second_number:
    print(True)
    third_number = int(input())
    if second_number < third_number:
        print(True)
    else:
        print(False)
else:
    print(False)
