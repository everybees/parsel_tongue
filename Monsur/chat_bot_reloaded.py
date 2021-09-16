import random
import datetime

dictionary = {
    "love":  ["yes, I love you!", "No, I don't love you!", "Nah!", "Love is wicked"],
    "age": [number for number in range(18, 50)],
    "country": ["France", "UK", "Nigeria"],
    "siblings": [number for number in range(1, 6)],
    "crazy": ["A lil", "Not at all", "Sometimes"],
    "relationship": ["Wow, even the gods do not know", "Yes, I am single", "It is complicated"],
    "eat": ["Yes, I have eaten"],
    "time": ['Time is: ', datetime.datetime.now().time()],
    "break": ["Yes, of course", "Nah!"],
    "happy": ["Yes", "No", "Maybe"],
    "why": ["Never mind!"]
    }
print("My name is Solibot, how can i help you?: ")
while True:
    user = input().split()
    if user == "exit":
        print("exiting...")
        break
    for keys, value in dictionary.items():
        if keys in user:
            print(random.choice(value))
            print("Ask another question")
            break
    else:
        print("I don't understand, try asking another question: ")









