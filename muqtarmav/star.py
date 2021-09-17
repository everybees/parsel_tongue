for row in range(1, 6):
    for column in range(0, row):
        print("*", end=" ")
    print("")
for row in range(5, 0, -1):
    for column in range(1, row):
        print("*", end=" ")
    print("")