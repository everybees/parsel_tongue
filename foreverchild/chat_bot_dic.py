import random
from typing import Dict, KeysView

print("Hello Ask me anything")



dict = {"love": ["yes", " i love you", " no, I dont love you", "what is love", "Love is wicked"],
"love": ["yes", " i love you", " no, I dont love you", "what is love", "Love is wicked"],
"name": ["My name is foreverchild What else can i help you with?"], 
 "eat": ["No, I haven't", "Yeah, I have had breakfast", "Yeah, I had eba and egusi", "No, I am fasting"], 
 "relationship": ["Wow, even the gods do not know", "Yes, i am single", "Yes, i am in a relationship", "its complicated"], 
 "feeling": ["I am feeling great today?", "i do not fall sick", "yes, a feeling of joy", "I am not happy",], 
 "feel": ["I am feeling great today?", "i do not fall sick", "yes, a feeling of joy", "I am not happy",], 
 "smart": ["Yes, i am smarter", "No am not as smart as you think", "I choose to be smart", "its better to be smart than to be dull"], 
 "rain": ["No its not gonna rain today", "I think i might rain", "yes just a bit", "no its sunny today"], 
 "come": ["yes I will be coming around", "Why do u need me arround?", "I will come", "No, Am busy"], 
 "angry": ["should be angry", "Always happy", "happiness makes you feel good", "I understand it is sad"], 
 "open": ["It is Open", "Failed to open", "too difficult to open", "I'll get it done"],
 "feel": ["I feel ok"]}

# ans = keyword.keys(random.choice(keyword))

# while True:
#     question = input()
#     for key, value in Dict.items():
#         if key in question:
#             print(random.choice(Dict[key]))
#             print("Ask me something else")
#             break
#     if "break" in question:
#         print("Bye Bye")
#         break
#     else:
#         print("I dont have a response to that, try something else")
#         # continue
                
while True:
    word = input().split()
    if ['exit'] == word:
        print("Exiting...")
        break

    option = []

    for wor in word:
        wor = wor.lower()
        if wor in dict.keys():
            option.append(random.choice(wor))
    if option:
            print(random.choice(option))
    else:
        print("I dont have a response to that, try something else")