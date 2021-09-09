row = 5
for i in range(0, row):
    for j in range(i, 0, -1):
        print('*', end=" ")
    print(" ")
rows = 4
for i in range(0, rows+1):
    for j in range(row-i, 0, -1):
        print("*", end=' ')
    print(" ")