digits = [1,2,3,4,5,6,7]

for a in range(len(digits)):
    for b in range(a):
        print("*", end=" ")

    print()

rows = 5
for a in range(0, rows+1):
    for b in range(rows-a, 0, -1):
        print("*", end=" ")

    print()