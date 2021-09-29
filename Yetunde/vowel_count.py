vowels = 'aeiou'
string = "eiagsjauapoeidneiaudkka"
count = 0
for _ in string:
    for vowel in vowels:
        if _ == vowel:
         count+=1
print(count)