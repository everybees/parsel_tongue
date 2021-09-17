
import datetime
import random
question = input()
love = ["yes, i love you!", "no, i dont love you", "what is love", "love is wicked"]
age = [num for num in range(1, 100)],
calculate =[3,4,6,7,8,9,],
sleep = ["What time do you sleep?", "How many hours do you sleep a day"],
exercise = ["Yes, I like exercise", "How even do you exercise?", "Exercise is good for your body"],
relationships = ["Wow even the gods do not know", "Yes, i am single"],
friendship = ["Hello, can i be your friend?", "No, i dont konw you", "How old are you", "Why do you ask", "Let me think abaout it"]

def do_something():
    question = input()
if "time" in question:
    print("The time is:", datetime.datetime.now().time())
elif "name" in question:
    print("My name is Precious, how can i help you?")
elif "old" in question or "age" in question:
    print("I am", random.choice(age), "years old")
elif "eat" in question or "eaten" in question:
    print("Yes, i have eaten.")   
elif "love" in question:
    print(random.choice(love))
elif "single" in question or 'relationship' in question:
    print(random.choice(relationships))  
elif "calculate" in question:
    print(random.choice(calculate))  
elif "sleep" in question:
    print(random.random(sleep))
elif "exercise" in question:
    print(random.choice(exercise))                 
else:
    print("I don't understand you. Do you mean what is the time of the day?")    