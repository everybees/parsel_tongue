import datetime
import random

print("This is Emmanuel. What question do you want answered today?")

love = ["Yes, I love you!", "No, I don't love you", "What is love?", "Love is wicked"]
age = [num for num in range(1, 100)]
eat = ["No, I haven't", "Yeah, I have had breakfast.", "Yeah, I had eba and egusi.", "No, I am fasting."]
relationship = ["wow, even the gods do not know.", "Yes, i am single", "Yes, I am in a relationship.", "It is complicated."]
sex = ["Male", "Female"]
language = ["English", "Yoruba", "Igbo", "Hausa"]
stateOfOrigin = ["Lagos", "Ogun", "Osun", "Oyo", "Ekiti"]

while True:
    question = input().split()
    if "time" in question:
        print("The time of day is:", datetime.datetime.now().time())
    elif "name" in question:
        print("My name is Emmanuel, How can i help you?")
    elif "old" in question or "age" in question:
        print("I am", random.choice(age), "years old")
    elif "eat" in question or "eaten" in question:
        print(random.choice(eat))
    elif "sex" in question:
        print(random.choice(sex))
    elif "language" in question:
        print(random.choice(language))
    elif "love" in question:
        print(random.choice(love))
    elif "stateOfOrigin" in question:
        print(random.choice(stateOfOrigin))
    elif "single" in question or "relationship" in question:
        print(random.choice(relationship))
    elif "break" in question:
        print("Seems you want to break up, Boy Bye!")
        break
    else:
        print("I don't understand you. Do you mean 'what is the time of the day?'")