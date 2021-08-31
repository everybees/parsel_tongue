import random
import datetime

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
         # "sharwarma": ["You want?", "Yes!", "Ole ni e", "Can we create a time for that?", "Ori e o pe!"],
         "how" and "are you": ["Fine", "Great", "Awwww.", "I need you", "I am fine"]
         }
    if "smart" in question:
        print(random.choice(b["smart"]))
    elif "name" in question:
        print(random.choice(b["name"]))
    elif "money" in question:
        print(random.choice(b["money"]))
    elif "food" in question:
        print(random.choice(b["food"]))
    elif "doing" in question:
        print(random.choice(b["doing"]))
    elif "shoe" in question:
        print(random.choice(b["shoe"]))
    elif "what" and "time" in question:
        print(random.choice(b["what" and "time"]))
    # elif "sharwama":
    #     print(random.choice(b["sharwarma"]))
    elif ("how" and "you") or "how are you":
        print(random.choice(b["how" and "are you"]))
    else:
        print("Can we say something else?")
    # # print(question)
    # love = ["Yes, I love you", "No, I don't love you", "What is love?", "Love is wicked"]
    # eat = ["I love food.", "Sapa, nice one"]
    # age = [num for num in range(1, 100)]
    # friend = ["I love friendships", "I will like to know you", "Friendship is key"]
    # money = ["I will like to know what you think", "Me sef. Sapa be doing the most", "I know you have money",
    #          "Is there something money cannot do?", "Come and gimme money"]
    # shoe = ["I am like Jona, I have no shoes", "Will like to get one", "Do you want to buy for me?",
    #         "Imagine walking with different shoes. Lol"]
    # food = ["Do you want Ogi?", "Food is not problem", "Do you mind me buying something for you?", "I need food too."]
    # smart = ["What?! We are all smart.", "Yes, if you think so.", "Well. Lol"]
    # doing = ["Nothing much", "Wise up", "No time oo", "Talking to you", "Sending videos to friends"]
    # # queyon = [love, eat, age, friend, money]

    # print(b[random.choice("love")])
    # if "what" and "time" in question:
    #     print("The time of the day is:", datetime.datetime.now().time())
    #     if "your name" in question:
    #         print("My name is Precious!")
    # elif "your name" in question:
    #     print("My name is Precious!")
    # elif "love" in question:
    #     print(random.choice(love))
    # elif "eat" in question:
    #     print(random.choice(eat))
    # elif "money" in question:
    #     print(random.choice(money))
    # elif "friend" in question:
    #     print(random.choice(friend))
    # elif "do" or "doing" in question:
    #     print(random.choice(doing))
    # elif "shoes" and "do" in question:
    #     print(random.choice(shoe))
    # elif "break" in question:
    #     break
    # else:
    #     print("I don't understand you.\nDo you mean What is the time of the day?")
    #     response = input()
    #     if "yes" in response:
    #         print("The time of the day is:", datetime.datetime.now().time())
    #     if "no" in response:
    #         print("Wahala ooo")
