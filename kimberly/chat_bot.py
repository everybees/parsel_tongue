# import datetime
# import random

# print("This is Precious. How can I help you today?")
# question = input()

# love = ["Yes, I love you!", "No, I don't love you", "What is love?", "Love is wicked!"]
# age = [num for num in range(1,100)]
# eat = ["No, I haven't.", "Yeah, I have had breakfast.", "No, I am fasting", "Yeah, I had pizza and icecream."]
# relationships= ["Wow, even the gods do not know.", "Yes, I am single.", "Yes, I am in a relationship", "It is complicated."]
# home= ["Yes i am.", "No, i'm not" ]
# visit = ["Don't even dare","Disembark from that nonsense capping", "It would be a pleasure"]
# music = ["hiphop is life!","rap is king!", "pop is my fav", "afrobeats for life"]
# dance = ["Lmao, I can't dance to save my life.", "I started dancing in my mother's womb.", "Dancing is my hobby", "I don't dance."]
# sleep = ["I am,I really need to go to bed now", "Yes, I am, Goodnight!", "No, I'm not", "Yes,i'll talk to you tomorrow"]



# while True:
#     question = input()
#     if "time" in question:
#         print("The time of day is:", datetime.datetime.now().time())
#     elif "name" in question:
#         print("My name is precious, How can i help you?")   
#     elif "old" in question or "age" in question:
#         print("I am", random.choice(age), "years old.")
#     elif "eat" in question or "eaten" in question:
#         print(random.choice(eat))
#     elif "love" in question:
#         print(random.choice(love))
#     elif "single" in question or "relationship" in question:
#         print(random.choice(relationships))
#     elif "home" in question or "alone" in question:
#         print(random.choice(home))
#     elif "visit" in question or "see" in question:
#         print(random.choice(visit)) 
#     elif "music" in question or "song" in question:
#         print(random.choice(music)) 
#     elif "dance" in question or "twerk" in question:
#         print(random.choice(dance))
#     elif "sleep" in question or "tired" in question:
#         print(random.choice(sleep))                 
#     elif "break" in question:
#         print("Seems you want to break up, Boy Bye!")
#         break  
#     else:
#h         print("I don't understand you. Do you mind asking another question?")                    

import datetime
import random 

# print("hi, i'm kim, what questions do you have for me today?")

my_first_dictionary = {
    "love":["Yes, I love you!", "No, I don't love you", "What is love?", "Love is wicked!"],
    "age":[num for num in range(1,100)],
    "eat":["No, I haven't.", "Yeah, I have had breakfast.", "No, I am fasting", "Yeah, I had pizza and icecream."],
    "relationship" :["Wow, even the gods do not know.", "Yes, I am single.", "Yes, I am in a relationship", "It is complicated."],
    "home":["Yes i am.", "No, i'm not" ],
    "visit":["Don't even dare","Disembark from that nonsense capping", "It would be a pleasure"],
    "music":["hiphop is life!","rap is king!", "pop is my fav", "afrobeats for life"],
    "dance":["Lmao, I can't dance to save my life.", "I started dancing in my mother's womb.", "Dancing is my hobby", "I don't dance."],
    "sleep":["I am,I really need to go to bed now", "Yes, I am, Goodnight!", "No, I'm not", "Yes,i'll talk to you tomorrow"],
    
}

def do_something():
    print("hi, i'm kim, what questions do you have for me today?")
    while True:

        question = input().split(" ")

        if "exit" in question:
            print("Goodbye, a'hole")
            break

        else:
            if "break" in question:
                print("Seems you want to break up, Boy Bye!")
                break            

            for key in question:
                if key in my_first_dictionary.keys():
                    print(random.choice(my_first_dictionary[key]))
                    break
                else:
                    print("I don't understand you, Do you mind asking another question? ")


do_something()