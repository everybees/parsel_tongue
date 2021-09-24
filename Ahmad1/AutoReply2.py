import random

options = {"dish": ["rice", "semo", "amala", "pounded yam", "porridge"],
           "reservation": ["yes, you can make a reservation", "you dont have a reservation", "No, not at the moment"],
           "drinks": ["long island", "juice", "wine", "champagne", "chapman"],
           "takeout": ["yes, take out is available", "Sorry, its not allowed"]
           }
print("Hello, my name is Alexa. how may i help you?")
while True:
    question = input().split()
    if "dish" in question:
        print(random.choice(options["dish"]))
    elif "reservation" in question:
        print(random.choice(options["reservation"]))
    elif "drinks" in question:
        print(random.choice(options["drinks"]))
    elif "takeout" in question:
        print(random.choice(options["takeout"]))
    elif "thanks" in question:
        print("i'm glad i could be of help. Do enjoy your meal")
        break
    else:
        print("i dont have an answer for that, kindly ask a different question")
