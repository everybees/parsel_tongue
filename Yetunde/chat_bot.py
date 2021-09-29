# chat bot to answer series of questions 
# questions: what is the time of the day?

import datetime
import random

print("This is presh. How may I help you?")
print("Type exit to quit.")

data = {"love" : ["Yes, I love you", "No, I don't love you", "love is wicked", "What is love"],
    "age": [num for num in range(1, 100)],
    "eat": ["No, I haven't", " Yeah , I have had breakfast", "Yes I am eaten"],
    "color": ["Blue", "Green", "Yellow", "White", "Red", "Violet", "Magenta", "pink"],
    "cake": ["Chocolate", "Red velvet", "Vanilla", "Strawberry", "Dessert Cake", "Marble Cake"],
    "country": ["United States", "Canada", "France", "Germany", "Australia", "Ghana", "South Africa", "Nigeria"],
    "food": ["Chicken and chips", "Sharwama", "Jollof rice", "Yam and egg", "Amala and ewedu", "Indomie"]
    }


while True:
    question = input().split()
    if ["exit"] == question:
        print("okay,bye!")
        break
    options = []

    for key in data:
        if key in question:
            options.append(random.choice(data[key]))
    if options:
        print(random.choice(options))
            
    else:
         print("I don't understand. Ask me something else")
   






    # if "time" in question:
    #      print("The time of the day is:", datetime.datetime.now().time())
    # elif "name" in question:
    #      print ("My name is Precious, How may i help you?")
    # elif "old" in question or "age" in question:
    #     print ("I am", random.choice(data["age"]), "years old")
    # elif "eat" in question or "eaten" in question:
    #     print(random.choice(data["eat"]))
    # elif "love" in question:
    #     print (random.choice(data["love"]))
    # elif "color" in question:
    #     print ("My best color is ",random.choice(data["color"]))
    # elif "cake" in question:
    #     print ("My favourite cake flavor is ",random.choice(data["cake"]))
    # elif "country" in question:
    #     print ("I would like to visit",random.choice(data["country"]))
    # elif "food" in question:
    #     print (random.choice(data["food"]))
    # elif "break" in question:
    #     print ("Seems you want to break up, Bye!")
    #     break
    # else:
    #  print(" I don't understand. Do you mind asking another question")


    