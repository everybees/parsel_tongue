import random

print("this is Bolu, what is your question please ask: ")

chat_bot_answers = {
    "love": ["yes, i love you", "No, i dont love you", "what is love", "love is wicked"],
    "age": [num for num in range(1, 50)],
    "eat": ["No, i haven't", "yeah, i have had breakfast", "yeah, i had eba and egusi", "no, i am fasting."],
    "ralationships": ["wow, even the gods do not know.", "yes, i am single", "yes, i am in a relationship",
                 "it is complicated"],
    "daddy_name": ["tife", "toye", "isreal", "dimeji"],
    "sex": [sex for sex in range(1, 10)],
    "mummy_name": ["mojoyin", "precious", "yetunde", "damilola"],
    "hobby": ["playing", "singing", "dancing", "jumping", "reading"],
    "style": ["missionary", "doggy", "619", "69", "jacki chan"],
}

# while True:
#     question = input().split("-")
#     for answer in question:
#         if answer in chat_bot_answers.keys():
#             print(random.choice(chat_bot_answers[answer]))
#         else:
#             print("i no understand waiting you they talk my guy")
#
#     if "break" in question:
#         print("i don break up")
#         break


while True:
    sentence = input().split()

    if ['exit'] == sentence:
        print("Exixting....")
        break

    options = []

    for word in sentence:
        word = word.lower()
        if word in chat_bot_answers.keys():
            options.append(random.choice(chat_bot_answers[word]))
    if options:
        print(random.choice(options))
    else:
        print("no match. ask another question")
