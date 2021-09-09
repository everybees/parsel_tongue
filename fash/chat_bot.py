import random
my_dictionary = {
"love" : ["Yes, I love you!","No, I don't love you", "What is love?", "Love is wicked"],
 "age": [num for num in range(1, 100)],
"eat": ["No, i haven't", "Yes I've heard breakfast", "I never chop"],
 "relationship": ["wow, even the gods are clueless", "Yes, i am single", "Yes, i am in a relationship"],
"sleep": ["I'm about to sleep", "I feel sleepy", "No I'm not"],
"kiss": ["I would love to kiss you", "Please send me a kiss emoji", "I am not romantic please, i am war"],
"sick":["I feel sick", "I hate hospitals", "I am love sick"],
"pray": ["Please pray for me"],
"break": ["break up"]
}
continue_chat = "yes"
while continue_chat == "yes":
    user = input()
    for keys, value in my_dictionary.items():
        if user in keys:
            print(random.choice(value))

    continue_chat = input("Enter yes to continue and no to break \n")
