import random
import datetime
import sys
collectables = {"love": ["love is like a dagger", "love is blind", "love is for the weak", "love is sweet"],
                "single": ["single is good", "in a single relationship", "living the big dream in my single days"],
                "eat": ["i just had a delicious meal", "food is what keeps the body fully functioning",
                        "you can not survive a day without food", "i am glad i have lots of food to consume"],
                "play": ["all work and no play really do not strengthen the mind",
                         "The art of cognitive thinking depends so much on the amount of fun put into work"],
                "marriage": ["A beautiful life time with someone special", "A community of people bond by blood",
                             "Living a life of responsibility"],
                "education": ["A special art of learning", "The art of developing the mind", "what would you love to "
                                                                                             "know about education"],
                "time": ["The time is " , datetime.datetime.now().time()],
                "name": ["why do you want to know my name", "Please tell me your name", "kindly introduce yourself",
                         "May i know your name too", "My name is chignons"],
                "school": ["Are you searching for the right school to send your ward",
                           "At Walmart our school system is the best in the world"],
                "restaurant": ["A place to order food", "There are 700 restaurants in labia street"]
                }

print("Hi, I am pretty smart, do you wanna test me out by asking some questions")
print()
while True:
    question = input("Kindly enter the question\n").split()

    for key, value in collectables.items():
        if key in question:
            print(random.choice(value))
            break

    else:
        print("I don't understand what you are saying. Do you mean...")
 