# chat bot to answer a series of questions
# chatbot name: precious
# question: what is the time? current time
# question 2: how old are you?
# question 3: have you eaten?
# question 4: do you love me?
# question 5: why am i still single?
#   question 6: when last did you sleep?
#   question 7: what do you love doing most?
#   question 8: what is your favourite song?
#   question 9: what is your favourite colour?
#   question 10: how old are you when you met your first love?
# question 11: what are you thinking about?

# answer: date and time of the day


import random
import datetime
from typing import Optional

print("My name is Precious. what questiion will you have answered today? ")

dictionary = {
    "love": ["Yes, I love you!","No i don't love you","what is love really?","Love is wicked"],
    "age": [num for num in range(1,100)],
    "old": [num for num in range(1,100)],
    "eaten": ["No, I haven't","Yeah, I have had breakfast","Yeah, I had Eba and egusi soup","No, I am fasting."],
    "relationship": ["wow, even the gods do not know.","Yes, I am single","Yes, I am in a relationship","It is complicated."],
    "sleep": ["It's really been long","I don't sleep at all","Being thinking all day",""],
    "song": ["No Gray by McReynold","Christ Representer by Jonathan McReynold","My Tomorrow","Fill me up","Frangrance of fire"],
    "doing_most":  ["Singing","Dancing","Coding","Reading","Gisting"],
    "colour": ["Purple","White","Blue"],
    "first_love":  [num for num in range(10,50)],
    "thinking":  ["Thinking of falling in love","Thinking of eating somthing nice","Thinking of you","Thinking about my life"]
}


# while True:
#     question = input().split(" ")
#     if "break" in question:
#         print("Seems you don't want to chat again, Boy bye!")
#         break
#     for word in question:
#      if word in dictionary.keys():
#         print(random.choice(dictionary[word]))
#         break    
#     else:
#         print("I don't understand you please. Do you mind aksing another question?")

while True:
    question = input().split()

    if ['exit'] == question:
        print("Existing...")
        break

    Options = []

    for word in question:
        word = word.lower()
        if word in dictionary.keys():
         Options.append(random.choice(dictionary[word]))
    if Options:
        print(random.choice(Options))
    else:
        print("No match. Kindly ask another question.")
       

# while True:
#    
#    if "time" in question:
#        print("The time of the day is:", datetime.datetime.now().time())
#    elif "name" in question:
#        print("My name is Precious, How can I help you?")
#    elif "old" in question or "age" in question:
#        print("I am", random.choice(age) ,"years old.")    
#    elif "eat" in question or "eaten" in question:
#        print(random.choice(eat))
#    elif "love" in question:
#        print(random.choice(love))
#    elif "single" in question or "relationship" in question:
#        print(random.choice(relationship))

#    elif "break" in question:
#        print("Seems you want to break up, Boy bye!")
#            

