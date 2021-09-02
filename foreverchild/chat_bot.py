#  chat bot to answer a seres of question

import datetime
import random

print("Hello my name is foreverchild! How may i help you?")

love = ["yes", " i love you", " no, I dont love you", "what is love", "Love is wicked"]
age = [num for num in range(1, 100)]
eat = ["No, I haven't", "Yeah, I have had breakfast", "Yeah, I had eba and egusi", "No, I am fasting"]
relationship = ["Wow, even the gods do not know", "Yes, i am single", "Yes, i am in a relationship", "its complicated"]
feeling = ["I am feeling great today?", "i do not fall sick", "yes, a feeling of joy", "I am not happy",]
Smart = ["Yes, i am smarter", "No am not as smart as you think", "I choose to be smart", "its better to be smart than to be dull"]
rain = ["No its not gonna rain today", "I think i might rain", "yes just a bit", "no its sunny today"]
come = ["yes I will be coming around", "Why do u need me arround?", "I will come", "No, Am busy"]
Angry = ["should be angry", "Always happy", "happiness makes you feel good", "I understand it is sad"]
open = ["It is Open", "Failed to open", "too difficult to open", "I'll get it done", ]

while True:
    question = input()
    if "love" in question:
        print(random.choice(love))
    elif "age" in question:
        print(random.choice(age))
    elif "eat" in question:
        print(random.choice(eat))
    elif "relationship" in question:
        print(random.choice(relationship))
    elif "felling" in question:
        print(random.choice(feeling))
    elif "smart" in question:
        print(random.choice(Smart))
    elif "rain" in question:
        print(random.choice(rain))
    elif "angry" in question:
        print(random.choice(Angry))
    elif "open" in question:
        print(random.choice(open))
    elif "come" in question:
        print(random.choice(come))
    elif question != input():
        print("am not sure i got your question")
    