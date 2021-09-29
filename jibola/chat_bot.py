# chat bot to answer a series of questions
# chatbot name: Precious

# question 1: what is the time? current time
# question 2: how old are you?  between 1 and 50
# question 3: have you eaten?   yes or no
# question 4: do you love me?   yes or no
# question 5: why am I still single?    one of many reasons

import datetime
import random

print("This is Precious. What question do you want answered today?")

love = ["Yes, I love you!", "No, I don't love you", "What is love?", "Love is wicked"]
age = [num for num in range(1, 100)]
eat = ["No, I haven't", "Yeah, I have had breakfast", "Yeah, I had eba and egusi", "No, I am fasting."]
relationships = ["Wow, even the gods do not know.", "Yes, i am single", "Yes, I am in a relationship", "It is complicated"]

while True:
    question = input()
    if "time" in question:
        print("The time of day is:", datetime.datetime.now().time())
    elif "name" in question:
        print("My name is Precious, How can I help you?")
    elif "old" in question or "age" in question:
        print("I am", random.choice(age), "years old.")
    elif "eat" in question or "eaten" in question:
        print(random.choice(eat))
    elif "love" in question:
        print(random.choice(love))
    elif "single" in question or 'relationship' in question:
        print(random.choice(relationships))
    elif "break" in question:
        print("Seems you want to break up, Boy Bye!")
        break
    else:
        print("I don't understand you. Do you mind asking another question?")
    
 