from Olatoye.new_specials import chatbot, calculator

if __name__ == "__main__":
    while True:
        userInput = int(input())
        if userInput == 1:
            calculator.calculator()
        elif userInput == 2:
            chatbot.chatbot()
