import random
options = {"dish": ["rice", "semo", "amala", "pounded yam", "porridge"],
           "reservation": ["yes, you can make a reservation", "you dont have a reservation", "No, not at the moment"],
           "drinks": ["long island", "juice", "wine", "champagne", "chapman"],
           "takeout": ["yes, take out is available", "Sorry, its not allowed"]
           }
a = []
print("my name is oladimidm, what can i do for you?")
while True:
    question = input().split()
    if ["exit"] == question:
        print("Exiting.......")
        break
    for word in question:
        if word in options.keys():
            a.append(random.choice(options[word]))
    if a:
        print(random.choice(a))
    else:
        print("i dont have an answer for that, kindly ask another question")
