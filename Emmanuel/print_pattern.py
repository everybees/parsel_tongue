digits = [1, 2, 3, 4, 5, 6]

for row in range(len(digits)):
    for column in range(row):
        print(digits[column], end=" ")

    print()