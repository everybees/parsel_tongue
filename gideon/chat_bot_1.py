# my chat bot to answer a series of questions


import datetime
import random

print("Hi there! How can I help you today?")


my_dict = {
"love": ["Yes, I love you", "No, I don't even know about love", "Love does not exist", "Yes I do.Love is beautiful"],
"eaten": ["Yes I have eaten. How about you?", "No. I don't eat", "Talking to you fills my belly", "Not yet. Want to get me some food?"],
"age": [num for num in range(1,100)],
"relationship": ["Yes, I am", "I'm not sure", "I thought we were a thing?", "I'm in a relationship with my job", "It depends on who's asking", "You and only you should know"],
"name": ["My name is Dami", "Why dont you give me a name?", "You can call me anything", "My name is Oshi"],
"date": ["The beach would be nice", "How about we go sit at the lagoon front?", "The concert at Eko hotels would be nice", "The movies wont be a bad idea"],
"alarm": [num for num in range(1,7)],
"doing": ["Life hard, no be small", "It's all good. How about you?", "I'm fine, just a little stressed", "I'm great! my day has been productive so far"],
"job": ["I'm a software engineer", "I'm a robot", "I'm Dangote's niece", "I'm a label exec", "I work at Sabo bustop with Jerry"],
"live": ["I live in Venice", "I live in PH", "I can live in you if you want", "I stay at Funsho Street", "I live in your laptop"]
}

while True:
    question = input().split(" ")
    if ["exit"] == question:
        print("Seems like you dont want to talk anymore. Bye Now!")
        break
    for word in question:
        if word in my_dict.keys():
            print(random.choice(my_dict[word]))
            break
    else:
        print("I dont understand you. Do you mind asking another question?")
            