import datetime
question = input('Ask a question:  ')  # .split()
# print(question)
if "what" and "time" in question:
    print("The time of the day is:", datetime.datetime.now().time())
    if "your name" in question:
        print("My name is Precious!")
elif "your name" in question:
    print("My name is Precious!")
else:
    print("I don't understand you.\nDo you mean What is the time of the day?")
    response = input()
    if "yes" in response:
        print("The time of the day is:", datetime.datetime.now().time())
    if "no" in response:
        print("Wahala ooo")