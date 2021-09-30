import random





love = ["No and I don't love you", "What is my Love status got to do with you", "Ask your MAMA", "I hate this question too muc"]
age = [num for num in range(1,100)]
eat = ["I was made not to eat", "I do not eat with poor people", "Fuck your food", "Baba free me i'm not eating", "FFO Oshi"]
relationship= ["Small child like you", "I'm sorry, I do not love poor people", "I hate when people ask", "A very Stupid Question"]

print("This is Funky, What question do you want answered today?")
question = input()
def do_something():
    while True:
        
        if "name" in question:
            print("My name is Funky, How Can I help you")
        elif "old" in question or "age" in question:
            print("I am", random.choice(age), "years old.")
        elif "eat" in question or "food" in question:
            print(random.choice(eat))
        elif "love" in question:
            print(random.choice(love))
        elif "single" in question or "relationship" in question:
            print(random.choice(single))
        elif "break"in question:
            print("seems you want to break up, Boy Bye")
        else:
            print("If you don't have any  question GTFOH!!! ")


