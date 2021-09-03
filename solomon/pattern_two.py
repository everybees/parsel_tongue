user_input = int(input("Enter number: \n"))
row = user_input

for e in range(row, 0, -1):
    for numbs in range(1, e+1):
        print(numbs, end='')
    print('')
