
import random
import datetime
Question = input("My name is Solibot, how can i help you?: ").split()
love = ["yes, I love you!", "No, I don't love you!", "Nah!", "Love is wicked"]
age = [number for number in range(18, 50)]
country = ["France", "UK", "Nigeria"]
siblings = [number for number in range(1, 6)]
crazy = ["A lil", "Not at all", "Sometimes"]
relationships = ["Wow, even the gods do not know", "Yes, I am single", "It is complicated"]


if "old" in Question or "age" in Question:
    print(random.choice(age))

elif "love" in Question:
    print(random.choice(love))

elif "eat" in Question or "eaten" in Question:
    print("Yes, I have eaten")

elif "time" in Question:
    print("Time is:", datetime.datetime.now().time())

elif "break" in Question:
    print("Yes of course!")

elif "single" in Question or "relationship" in Question:
    print("Nah! I am not")

elif "happy" in Question:
    print("Yes now!")

elif "country" in Question:
    print(random.choice(country))

elif "number" in Question or "phone number" in Question:
    print("07058029688")

elif "siblings" in Question:
    print(random.choice(siblings))

elif "crazy" in Question or "craze" in Question:
    print(random.choice(crazy))

else:
    print("I don't understand you.")
