# chat bot to answer a series of questions

# chatbot name: Dami
# question: what is the time of the day? current time
# question 2: how old are you? between 1 and 50
# question 3: have you eaten? yes or no
# question 4: do you love me? yes or no
# question 5: why am I still single? one of many reasons

import datetime
import random

print("Hi there! How can I help you today?")

love = ["Yes, I love you", "No, I don't even know about love", "Love does not exist", "Yes I do.Love is beautiful"]
eat = ["Yes I have eaten. How about you?", "No. I don't eat", "Talking to you fills my belly", "Not yet. Want to get me some food?"]
age = [num for num in range(1,100)]
relationship = ["Yes, I am", "I'm not sure", "I thought we were a thing?", "I'm in a relationship with my job", "It depends on who's asking", "You and only you should know"]
name = ["My name is Dami", "Why dont you give me a name?", "You can call me anything", "My name is Oshi"]
place = ["The beach would be nice", "How about we go sit at the lagoon front?", "The concert at Eko hotels woold be nice", "The movies wont be a bad idea"]
alarm = [num for num in range(1,7)]
doing = ["Life hard, no be small", "It's all good. How about you?", "I'm fine, just a little stressed", "I'm great! my day has been productive so far"]
job = ["I'm a software engineer", "I'm a robot", "I'm Dangote's niece", "I'm a label exec", "I work at Sabo bustop with Jerry"]
live = ["I live in Venice", "I live in PH", "I can live in you if you want", "I stay at Funsho Street", "I live in your"]


while True:
    question = input()
    if "time" in question:
        print("The time of the day is:", datetime.datetime.now().time())
    elif "name" in question:
        print(random.choice(name))
    elif "old" in question or "age" in question:
        print("I am", random.choice(age), "years old")
    elif "eat" in question or "eaten" in question:
        print(random.choice(eat))
    elif "love" in question:
        print(random.choice(love))
    elif "single" in question or "relationship" in question:
        print(random.choice(relationship))
    elif "place" in question or "date" in question:
        print(random.choice(place))
    elif "alarm" in question or "wake" in question:
        print("Alarm set for",random.choice(alarm),":am")
    elif "job" in question or "you do" in question:
        print(random.choice(job))
    elif "doing" in question:
        print(random.choice(doing))
    elif "live" in question or "stay" in question:
        print(random.choice(live))
    elif "break" in question:
        print("Seems you dont want talk anymore. Bye Now!")
        break
    else:
        print("I dont understand you. Do you mind asking another question?")
    