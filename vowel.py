string = input("enter words ")
vowels = 0
for vowel in string:
    if vowel == 'a' or vowel == 'e' or vowel == 'i' or vowel == 'o' or vowel == 'u':
        vowels = vowels + 1
print("total number of vowels are ")
print(vowels)
