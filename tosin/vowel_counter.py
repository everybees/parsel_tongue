string = "red color means danger"
vowel = 'aeiou'
number = 0
for i in string:
    for r in vowel:
        if i == r:
            number += 1
print(number)
