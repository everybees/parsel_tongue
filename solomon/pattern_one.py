user_input = int(input("Enter number: \n"))
row = user_input

for numb in range(row+1):
    for numbs in range(numb):
        print(numb, end='')
    print('')