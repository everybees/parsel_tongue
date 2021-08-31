red = 5
for i in range(red):
    for j in range(i + 1):
        print('*', end=" ")
    print()
row = 4
for i in range(0, row + 1):
    for j in range(row - i, 0, -1):
        print('*', end=" ")
    print()