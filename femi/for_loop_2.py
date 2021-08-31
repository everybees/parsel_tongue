speech = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
text = input()
for t in text:
    for s in range(len(speech)):
        if int(t)==s:
            print(speech[s])