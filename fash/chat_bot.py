import random
import datetime
# question 1: what is the current time
# question 2: how old are you? between 1 and 50
#  question 3: do you love me: yes or no
#  question 4: have you eaten?




love = ["Yes, I love you!","No, I don't love you","What is love?","Love is wicked"]
age = [num for num in range(1,100)]
eat = ["No, i haven't","Yes I've heard breakfast","I never chop"]
relationships =["wow, even the gods are clueless","Yes, i am single","Yes, i am in a relationship"]
sleep = ["I'm about to sleep","I feel sleepy", "No I'm not"]
kiss = ["I would love to kiss you","Please send me a kiss emoji", "I am not romantic please, i am war"]
sick = ["I feel sick","I hate hospitals","I am love sick"]
pray = ["Please pray for me"]
while True:
    question = input("I am Israel, what's up:")
    if "time" in question:
        print("The time of the day is :", datetime.datetime.now().time())
    elif "name" in question:
        print("My name is Israel, How can i help you")
    elif "old" in question or "age" in question:
        print(random.choice(age))
    elif "eat" in question or "eaten" in question:
        print(random.choice(eat))
    elif "love" in question:
        print(random.choice(love))
    elif "single" in question:
        print(random.choice(relationships))
    elif "sleep" in question or "tired" in question:
        print(random.choice(sleep))
    elif "kiss" in question or "sex" in question:
        print(random.choice(kiss))
    elif "sick" in question or "ill" in question:
        print(random.choice(sick))
    elif "pray" in question or "prayer" in question:
        print(random.choice(pray))
        break
    else:
        print("I don't understand you. Do you mind asking another question")


# Assignment
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
