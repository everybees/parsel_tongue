row = 5
for i in range(0, row + 1):
    for j in range(row - i, 0, -1):
        print(j, end=" ")
    print()