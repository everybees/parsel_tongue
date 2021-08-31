# number = [1, 2, 3, 4, 5, 6]

# for i in range(len(number)):
#     for j in range(i):
#         print(number[j], end=" ")

#     print()

# #number =[5,4,3,2,1]

rows = 5
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print('')