import datetime
import random

print(datetime.datetime.now())
dicts = {


        "automobile": ["Tesla", "Benz", "Porsche "],
        "sport": ["football", "basketball", "Tennis", "Cricket"],
        "continent": ["Africa", "Europe", "North America", "South America", "Antarctica", "Asia"],
        "Tribes": ["Yoruba", "Igbo", "Hausa"],
        "brand": ["louis vuitton", "Armani", "Versace"],
        "relationship": ["Even the gods do not know", "Yes, I'm single", "Its complicated"],
        "artist": ["Bryson tiller", "Drake", "Wizkid", "Trey songz"],
        "player" : ["Ronaldo", "Messi"],
        "language":  ["English", "French", "Yoruba", "Spanish"],
        "richest":  ["Muqtar", "Elon Musk", "Bill gates", "Jeff Bezos"],

}

print("this is mav", "ask your question")
while True:
    question = input().split()
    if "automobile" in question:
        print(random.choice(dicts["automobile"]))
    elif "sport" in question:
        print(random.choice(dicts["sport"]))
    elif "continent" in question:
        print(random.choice(dicts["continent"]))
    elif "tribes" in question:
        print(random.choice(dicts["tribes"]))
    elif "brand" in question:
        print(random.choice(dicts["brand"]))
    elif "Richest" in question:
        print(random.choice(dicts["richest"]))
    elif "artist" in question:
        print(random.choice(dicts["artist"]))
    elif "player" in question:
        print(random.choice(dicts["player"]))
    elif "language" in question:
        print(random.choice(dicts["language"]))
    elif "break" in question or "stop" in question:
        print("it seems you are no longer interested in the question, "  'boy bye!')
        break
    else:
        print("I don't understand you, Do you mean 'what is the time of the day?    '")








