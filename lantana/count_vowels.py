print("Please input your sentence!")
words = input()
vowels = "aeoui"
count=0

for i in words:
    if i in vowels:
        count+=1
print(count)