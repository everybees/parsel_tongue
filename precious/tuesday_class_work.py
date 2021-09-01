# chatbot to answer series of questions
# chat_bot name : precious
# answer : date and time of day
# question_1: what is the time of the day?
# question_2: how old are you?
# question_3: how old are you?
# question_4: do you love me? yes or no
# question_5: why am i still single?
import datetime
import random

love = ["Yes, i love you", "No, I dont love you", "What is love?", "love is wicked"]
name = ["my name is precious", "my name is amarachi", "my name is lois", "my name is delight", "daniel", "jahson",
        "jahzeal", "jada"]
age = [number for number in range(1, 100)]
relationship = ["i am single", "i am not single", "i am married", "i am not married", "i am engaged", "i am not engaged"
                , "its complicated", "i am confused"]
eaten = [" no i have not eaten", "i'm actually starving", "Yes i have eaten"]
eat = ["i ate eba and egusi soup", "i ate rice and stew", "i drank garri", "jelof rice"]
happy = ["Yes i am happy been your best_friend", "No i am not happy because you are too busy to play with me"]
friends = ["Yes we can be best buddies", " Yes i would love that too", "No please i'm too busy to have a friend"]
gender = ["female", "male", "transgender"]
love_me = ["i dont love you because you ugly", ("i dont love you because i love", random.choice(name)),
           "i love because you the best"]
nice_to_meet_you = ["the pleasure is all mine", "i dont know you but i hate you already"]
why_you_still_single = ["men are scam", "i found love once and then i lost him to other bitch"]

print("This is ", random.choice(name), "How may i be of help to you")

while True:
    question = input().split("-")
    if "name" in question:
        print(random.choice(name))

    elif "time" in question or "date" in question:
        print("The time of day is: ", datetime.datetime.now().time())

    elif "age" in question or "old" in question:
        print(random.choice(age))

    elif "love" in question:
        print(random.choice(love))

    elif "love me" in question:
        print(random.choice(love_me))

    elif "relationship" in question or "single" in question or "married" in question:
        print(random.choice(relationship))

    elif "eaten" in question:
        print(random.choice(eaten))

    elif "eat" in question:
        print(random.choice(eat))

    elif "happy" in question:
        print(random.choice(happy))

    elif "still single" in question:
        print(random.choice(why_you_still_single))

    elif "friends" in question:
        print(random.choice(friends))

    elif "nice to meet you" in question or "nice meeting you" in question:
        print(random.choice(nice_to_meet_you))

    elif "gender" in question or "sex" in question:
        print(random.choice(gender))

    elif "break" in question:
        print("seem like this relationship is not working and you want to break up bye its was fun while its lasted")
        break
    else:
        print("i dont understand your question, mind asking a different question?")

