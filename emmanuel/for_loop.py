# string = ""
# for i in range(1, 20, 4):
#     string += "&" * i
# print(string)

#
# for x in range(1, 4):
#     for y in range(-3, 0):
#         print(x * y)

# string = "red yellow fox bite orange goose beeeeeeeeeeep"
# vowels = 'aeiou'
# counter = 0
#
# for vowels in string:
#     if vowel in vowels:
#         counter +=1
#         print(counter)

# numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
#
# digits = input()
#
# for digit in digits:
#     print(digit, ":", numbers[int(digit)], end=" ")  # end is a key word to help you print on string. on a straigth line

a = [1, 2, 3, 4, 5]
b = "12345"
c = 23

if len(b)>4:
    for i in range(len(a)):
        if c < 20:
            print("a")
        else:
            for j in a:
                print(j,i)
    while c>15:
        for i in a:
            print(i**i)
            c-=1