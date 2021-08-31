# first list the numbers
# next get the index of each number
# find a way to loop the index in decremental order
# this becomes the smaller loop
# the bigger loop still decrements by one after the smaller
#   loop has executed

numbers = '54321'
index = 0
for index in range(len(numbers)):
    while index < 5:
        print(numbers[index], end=" ")
        index += 1
    print()
