from jibola import chat_bot

if __name__ == "__main__":
    number = int(input("enter a number: "))
    if number == 1:
        chat_bot.do_something(4)
    else:
        print("please enter 1")
