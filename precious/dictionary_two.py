import random
import datetime

array_list = {

    "time": ["The time of day is: ", datetime.datetime.now().time()],
    "love": ["Yes, i love you", "No, I dont love you", "What is love?", "love is wicked"],
    "name": ["precious", "amarachi", "lois", "delight", "daniel", "jahson", "jahzeal", "jada"],
    "old": [number for number in range(1, 100)],
    "relationship": ["i am single", "i am not single", "i am married", "i am not married", "i am engaged",
                     "i am not engaged", "its complicated", "i am confused"],
    "eaten": [" no i have not eaten", "i'm actually starving", "Yes i have eaten"],
    "eat": ["i ate eba and egusi soup", "i ate rice and stew", "i drank garri", "jollof rice"],
    "happy": ["Yes i am happy been your best_friend", "No i am not happy because you are too busy to play with me"],
    "friends": ["Yes we can be best buddies", " Yes i would love that too",
                "No please i'm too busy to have a friend"],
    "gender": ["female", "male", "transgender"],
    "hate": ["i dont love you because you ugly", "i dont love you because i love " + random.choice("name"),
             "i dont love because you're not my best friend"],
    "meet": ["the pleasure is all mine", "i dont know you but i hate you already"],
    "why": ["men are scam", "i found love once and then i lost him to other bitch"],
    "country": ["uk", "Nigeria", "USA", "Canada", "Germany", "france", "Ghana", "India"],
    "exit": ["seem like this relationship is not working and you want to break up bye it was fun while its lasted"]
}
print("Hello, my name is ", random.choice(array_list["name"]), "How may i be of help to you")
while True:

    search = input().split()

    if ['exit'] == search:
        print("Exiting....")
        break

    options = []

    for word in search:
        word = word.lower()
        if word in array_list.keys():
            options.append(random.choice(array_list[word]))
    if options:
        print(random.choice(options))
    else:
        print("i no dey hear english. Try again later")
