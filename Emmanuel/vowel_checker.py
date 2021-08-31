from typing import Counter


vowel = "aeiou"

given = input()

Count = 0
for a in given:
    if a in vowel:
        Count = Count + 1
        print(Count)