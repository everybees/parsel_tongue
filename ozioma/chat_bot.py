import random
import datetime
question = input('Ask a question:  ')  # .split()
# print(question)
love =["Yes, I love you", "No, I don't love you", "What is love?", "Love is wicked"]
if "what" and "time" in question:
    print("The time of the day is:", datetime.datetime.now().time())
    if "your name" in question:
        print("My name is Precious!")
elif "your name" in question:
    print("My name is Precious!")
elif "love" in question:
    print(random.choice(love))
else:
    print("I don't understand you.\nDo you mean What is the time of the day?")
    response = input()
    if "yes" in response:
        print("The time of the day is:", datetime.datetime.now().time())
    if "no" in response:
        print("Wahala ooo")
