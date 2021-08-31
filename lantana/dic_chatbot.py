import random

data = {
    "love" : ["yes,i love you","No,i dont love you","what is love","Love is wicked"],
    "age": [num for num in range(1,100)],
    "eat": ["No,i have not eaten","Yes,i have eaten","No,iam not hungry"],
    "relationships": ["wow,even the gods does not know","yes,i am single","yes,i am in a relationship","it is complicated"],
    "states": ["Lagos","Kogi","Abuja","Calabar"],
    "schools": ["unilag","oou","university of ibadan"],
    "courses": ["medicine", "law","botany","sofeware-engineering"],
    "married": ["no,i am not married","yes,i am married","i am divorced"],
    "travelling": ["yes,i love travelling","No,i dont like travelling","travelling is fun"]
    }

question = input().split()
for q in question:
    if q in data.keys():
        print(random.choice(data[q]))

