import datetime
import random


print("Hi!, How can i help you today?")

my_dict = {
"love": ["Yes, I love you!", "No, I don't love you", "What is love?", "Love is wicked"],
"age": [num for num in range(1, 100)],
"eat": ["No, I haven't", "Yeah, I have had breakfast.", "Yeah, I had eba and egusi.", "No, I am fasting."],
"relationship": ["wow, even the gods do not know.", "Yes, i am single", "Yes, I am in a relationship.", "It is complicated."],
"sex": ["Male", "Female"],
"language": ["English", "Yoruba", "Igbo", "Hausa"],
"stateOfOrigin": ["Lagos", "Ogun", "Osun", "Oyo", "Ekiti"]
}

while True:
    question = input().split("_")
    for word in question:
        if word in my_dict:
            print(random.choice(my_dict[word]))
        else:
            print("I don't understand you. Do you mind asking another question?")
        if "break" in question:
            print("seems you don't want to talk. bye for now")
            break