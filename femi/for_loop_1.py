vowel= "aeiou"
given= "baeocdfgh"
count=0
for i in given:
    if i in vowel:
        count=count+1
print(count)