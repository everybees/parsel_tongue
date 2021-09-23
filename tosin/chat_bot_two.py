import datetime
import random
response = {
    'love' : ["Yes, I love you", "No, I don't love you", "What is love", "Love is wicked"],
    'age' : [num for num in range(1,100)],
    'relationships' : ["Wow, even the gods do not know.", "Yes, I'm single", "Yes, I'm in relationship", "It is complicated"],
    'eat' : ["I haven't", "Yeah, I have had dinner", "Yeah, I have had my breakfast", "I have eaten"],
    'weather' : ["It is sunny", "It is cloudy", "snowing", "raining"],
    'location' : ["Lagos", "Abuja", "Benin", "Ibadan"],
    'feelings' : ["I'm good", "I'm happy", "I'm tired", "I'm feeling great"],
    'shopping' : ["Yes", "No"],
    'days' : ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    
}


def do_something():
    print("I'm Muqtar. What question do you want answered today?")
    while True:
        question = input().split()
        if ['exit'] == question:
            print("Exiting...")
            break
        options = []
        for word in question:
            if word in response.keys():
                options.append(random.choice(response[word]))
                #print(random.choice(response[word]))
        if options:
            print(random.choice(options))
        else:
            print("You said what? please make me understand")
