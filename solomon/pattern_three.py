user_input = int(input("Enter number: \n"))
row = user_input

for numb in range(0, row):
    for numbs in range(0, numb+1):
        print("*", end='')
    print('')


for e in range(row, 0, -1):
    for numbs in range(0, e+1):
        print("*", end='')
    print('')
