a = 5
for row in range(0,a+1):
    for column in range(a - row, 0, -1): 
        print(column, end=" ")
    print()