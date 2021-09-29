import datetime
import random

print(datetime.datetime.now())
dicts = {


        "automobile": ["Tesla", "Benz", "Porsche "],
        "sport": ["football for sure 'its the most famous' ", "basketball", "Tennis", "Cricket"],
        "continent": ["Africa", "Europe", "North America", "South America", "Antarctica", "Asia"],
        "Tribes": ["Yoruba", "Igbo", "Hausa"],
        "brand": ["louis vuitton", "Take a guess", "Armani", "Versace"],
        "relationship": ["Even the gods do not know", "Yes, I'm single", "Its complicated"],
        "artist": ["Bryson tiller", "Drake", "Wizkid", "Trey songz"],
        "player": ["Ronaldo", "Messi"],
        "language":  ["I like English and French", "Yoruba is nice"  "Spanish"],
        "richest":  [" Sir Muqtar for sure", "Take a guess ? " "Elon Musk", "Bill gates", "Jeff Bezos"],

}

print("this is mav", "ask your question")
while True:
    question = input().split()
    if ['exit'] == question:
        print("Existing...")
        break
    options = []
    for word in question:
        if word in dicts.keys():
         options.append(random.choice(dicts[word]))
    if options:
        print(random.choice(options))
    else:
        print("you said what, make me understand")





