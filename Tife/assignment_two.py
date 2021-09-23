# #text-to-speech
# input = input("Enter a number: ")
# numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
# for elements in input:
#     print("This is", numbers[int(elements)], end="\n")


# Vowel Hunter 
# string = input("Enter a word:\n")
# vowels = 'aeiou'
# counter = 0
# for letters in string:
#     if letters in vowels:
#         counter +=1
#         print(counter, end=" ")

#numbers_r>_triangle
# a = [1,2,3,4,5,6]
# for row in range(len(a)):
#     for column in range (row):
#         print (a[column], end=" ")

#     print()    

#numbers_r>_triangle (inverted)
# number = [1,2,3,4,5]
# for rows in range(len(number), 0, -1):
#     for columns in range(1, rows + 1):
#         print(columns, end=' ')
#     print('\r')


a = [1,2,3,4,5,6]
for row in range(len(a)):
    for column in range (row):
        print ("*", end=" ")

    print()

for rows in range(len(a), 0, -1):
    for columns in range(1, rows + 1):
        print("*", end=' ')
    print('\r')