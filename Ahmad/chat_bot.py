import datetime
import random

love = ["Yes, i love you.", "No, i dont love you.", "love is wicked", "What is love?"]
age = [num for num in range(1, 100)]
relationship = ["yes, i am single", "yes, i am in a relationship", "it is complicated", "i am married"]
print("This is chat Box, what question would you like answered today?")
while True:
    question = input().split()
    if "time" in question:
        print("the time of the day is: ", datetime.datetime.now().time())
    elif "name" in question:
        print("my name is Precious, How can i help you?")
    elif "eat" in question or "eaten" in question:
        print("yes, i have eaten.")
    elif "love" in question:
        print(random.choice(love))
    elif "age" in question or "old" in question:
        print("i am", random.choice(age), "years old")
    elif "relationship" in question:
        print(random.choice(relationship))
    elif "break" in question:
        print("seems you want to break up, Boy Bye!")
        break
    else:
        print("i dont understand you. Do you mind asking another question?")
