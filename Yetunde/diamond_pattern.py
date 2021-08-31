rows = 5
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print('*', end=' ')
    print('')
number = 6
for i in range(1, number):
    for j in range(number -i, 0, -1):
        print('*', end=' ')
    print(' ')