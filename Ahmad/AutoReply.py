import random
print("Hello, this is Alex. Lets have a discussion!!")
admission = ["Did you get admitted?", "Admission is over", "Admission is in progress", "Admission is by merit"]
scholarship = ["We offer fully funded scholarships", "Scholarships are not available", "We only offer partial scholarships"]
waiver = ["waiver is available", "Sorry, no application fee waiver", "kindly send an email to the grad coordinator"]
Bioinformatics = ["yes, the program is available", "No, the program is not available"]
while True:
    question = input().split()
    if "admission" in question:
        print(random.choice(admission))
    elif "scholarship" in question:
        print(random.choice(scholarship))
    elif "waiver" in question or "fee" in question:
        print(random.choice(waiver))
    elif "Bioinformatics" in question:
        print(random.choice(Bioinformatics))
    elif "Thanks" in question:
        print("I'm glad i could be of help. Take care!!")
        break
    else:
        print("Sorry, i dont have an answer for that. kindly ask another question.")