vowels = ["A","E","I","O","U"]

count = 0

word = input("Enter the Word" + " ")

for vowel in word:
    if (vowel.upper() in vowels):
        count += 1

print(count)
