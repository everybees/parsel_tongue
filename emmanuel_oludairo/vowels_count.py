string = "red yellow fox bite orange goose beeeeeeeeep"
vowels = 'aeiou'
counter = 0

for vowels in string:
    if vowels in vowels:
        counter +=1
print(counter)