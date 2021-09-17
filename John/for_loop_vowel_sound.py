vowel = "aeiou"
counter = 0;
user_response = input("enter the word to determine its number of  vowel letter  ")
for i in user_response:
    if i in vowel:
        counter += 1
print(counter)