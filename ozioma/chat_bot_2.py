import random
import datetime


def do_somthing():
    while True:
        question = input('Ask a question:  ').split()
        b = {"what" and "time": ["The time of the day is:", datetime.datetime.now().time()],
             "name": ["My name is Precious!"],
             "love": ["Yes, I love you", "No, I don't love you", "What is love?", "Love is wicked"],
             "money": ["I will like to know what you think", "Me sef. Sapa be doing the most", "I know you have money",
                       "Is there something money cannot do?", "Come and gimme money"],
             "shoe": ["I am like Jona, I have no shoes", "Will like to get one", "Do you want to buy for me?",
                      "Imagine walking with different shoes. Lol"],
             "food": ["Do you want Ogi?", "Food is not problem", "Do you mind me buying something for you?",
                      "I need food too."],
             "smart": ["What?! We are all smart.", "Yes, if you think so.", "Well. Lol"],
             "doing": ["Nothing much", "Wise up", "No time oo", "Talking to you", "Sending videos to friends"],
             "do": ["Nothing much", "Wise up", "No time oo", "Talking to you", "Sending videos to friends"],
             "shawarma": ["You want?", "Yes!", "Ole ni e", "Can we create a time for that?", "Ori e o pe!"],
             "how" or "are you": ["Fine", "Great", "Awwww.", "I need you", "I am fine"]
             }
        if "break." in question:
            break

        for word in question:
            if word in b:
                print(random.choice(b[word]))
                break
            elif word not in b:
                print("I don't understand you! New question please.")
                break
