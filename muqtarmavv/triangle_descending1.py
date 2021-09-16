rows = int(input("enter number of rows: "))
for i in range(rows, 0, - 1):
    for columns in range(i, 0, -1):
        print(columns, end="")
    print("")
