#chat bot to answer a series of question
#Twhat is ime of the day
#How old are you
#what your relationship status
#who is your favorite artist
#who is the best player
#whats your preferred language
#who is the richest man on earth
#chatbot name
import datetime
import random

print(datetime.datetime.now())
love = ["yes, I love you", "No, I don't love you", "love don't exist", "No love is wicked"]
age = [num for num in range(1, 100)]
relationship = ["Even the gods do not know", "Yes, I'm single", "Its complicated"]
artist = ["Bryson tiller", "Drake", "Wizkid", "Trey songz"]
player = ["Ronaldo", "Messi"]
language = ["English", "French", "Yoruba", "Spanish"]
richest = ["Muqtar", "Elon Musk", "Bill gates", "Jeff Bezos"]

print("this is Precious", "ask your question")
while True:
    question = input().split()
    if "time" in question:
        print("the time of day is", datetime.datetime.now().time())
    elif "name" in question:
        print("my name is precious, how can i help you")
    elif "single" in question or "relationship" in question:
        print(random.choice(relationship))
    elif "love" in question:
        print(random.choice(love))
    elif "age" in question or "old" in question:
        print(random.choice(age))
    elif "country" in question or "from" in question:
        print("I'm from London")
    elif "Richest" in question:
        print(random.choice(richest))
    elif "artist" in question:
        print(random.choice(artist))
    elif "player" in question:
        print(random.choice(player))
    elif "language" in question:
        print(random.choice(language))
    elif "break" in question or "stop" in question:
        print("it seems you are no longer interested in the question, "  'boy bye!')
        break
    else:
        print("I don't understand you, Do you mean 'what is the time of the day?    '")
