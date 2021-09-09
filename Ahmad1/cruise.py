import random

options = {"dish": ["rice", "semo", "amala", "pounded yam", "porridge"],
           "reservation": ["yes, you can make a reservation", "you dont have a reservation", "No, not at the moment"],
           "drinks": ["long island", "juice", "wine", "champagne", "chapman"],
           "takeout": ["yes, take out is available", "Sorry, its not allowed"]
           }
print("my name is oladimdim, how can i help you?")
while True:
    question = input().split()
    for word in question:
        if word in options.keys():
            print(random.choice(options[word]))
            break
    else:
        print("i dont have an answer for that, kindly ask a different question")
