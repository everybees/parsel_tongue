#chat bot to answer a series of question
#1. Time of the day
#chatbot name: Precious
#answer: date and time of day
#question 2: how old are you:
#question 3: have you eaten? yes or no
#question 4: 
#question 5:
#type(a) is type(b)

import datetime
import random
love = ["Yes, I love you", "No, I don't love you", "What is love", "Love is wicked"]
age = [num for num in range(1,100)]
relationships = ["Wow, even the gods do not know.", "Yes, I'm single", "Yes, I'm in relationship", "It is complicated"]
eat = ["I haven't", "Yeah, I have had dinner", "Yeah, I have had my breakfast", "I have eaten"]
weather = ["It is sunny", "It is cloudy", "snowing", "raining"]
locations = ["Lagos", "Abuja", "Benin", "Ibadan"]
feelings = ["I'm good", "I'm happy", "I'm tired", "I'm feeling great"]
shopping = ["Yes", "No"]
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
print("This is Precious. What question do you want answered today?")

while True:
    question = input().split()
    if "time" in question:
        print("The time of the day is:", datetime.datetime.now().time())
    elif "name" in question:
        print("My name is Precious, How can I help you?")
    elif "old" in question or "age" in question:
        print("I am 20 years. How old are you?")
    elif "eat" in question or "eaten" in question:
        print(random.choice(eat))
    elif "love" in question:
        print(random.choice(love))
    elif "single" in question or "relationship" in question:
        print(random.choice(relationships))
    elif "break" in question or "up" in question:
        print("It seems you no longer show interest in the conversation, boy Bye!")
        break
    elif "weather" in question:
        print(random.choice(weather))
    elif "location" in question or "where":
        print(random.choice(locations)) 
    elif "feeling" in question:
        print(random.choice(feelings))
    elif "shopping" in question:
        print(random.choice(shopping))
    elif "day" in question:
        print(random.choice(days)) 
    else:
        print("I don't understand you. Ask another question")
