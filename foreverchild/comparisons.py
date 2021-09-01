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
