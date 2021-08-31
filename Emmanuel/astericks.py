digits = 7

for row in range(0, digits+1):
    for column in range(row):
        print("*", end=" ")

    print()

a = 6
for row in range(0,a+1):
    for column in range(a - row, 0, -1): 
        print("*", end=" ")
    print()


    