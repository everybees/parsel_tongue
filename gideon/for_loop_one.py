string = input("Enter a phrase: ")
vowels = "aeiou"
vowel_checker = 0

for n in string:
    if n in vowels: 
        vowel_checker += 1

print(vowel_checker)


# for count in range(2):
#     number = int(input())
#     if number%2 == 0:
#         print("Number is even")
#     else:
#         print("Number is odd")
