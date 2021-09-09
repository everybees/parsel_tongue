#chatbot to answer series of question

#uestion 1: what is the time
#question 2: what is your name?
#question 3: How old are you?
#question 4: Have you eaten
import datetime
import random

question = input().split()
love = ["yes,i love you","No,i dont love you","what is love","Love is wicked"]
age = [num for num in range(1,100)]
eat = ["No,i have not eaten","Yes,i have eaten","No,iam not hungry"]
relationships = ["wow,even the gods does not know","yes,i am single","yes,i am in a relationship","it is complicated"]
states = ["Lagos","Kogi","Abuja","Calabar"]
schools = ["unilag","oou","university of ibadan"]
courses = ["medicine", "law","botany","sofeware-engineering"]
married = ["no,i am not married","yes,i am married","i am divorced"]
travelling = ["yes,i love travelling","No,i dont like travelling","travelling is fun"]

while True:
    question = input()
    
    if "time" in question:
        print("The time of the day is:", datetime.datetime.now().time()) 
    elif "name" in question:
         print("My name is Lantana, How can i help you")
    elif "state" in question:
        print("i am from",random.choice9(states),"state")
    elif "old" in question or "age" in question:
        print("i am", random.choice(age), "years old")
    elif "school" in question:
        print("i ama graduate of",random.choice(schools))
    elif "course" in question:
        print("i studied",random.choice(courses))
    elif "eat" in question or "eaten" in question:
        print(random.choice(eat))
    elif "married" in question:
        print(random.choice(married))
    elif "travel" in question or "travelling" in question:
       print(random.choice(travelling))
    elif "love" in question:
        print(random.choice(love))
    elif "single" in question:
         print(random.choice(relationships))
    elif "break" in question:
        print("Seems you want to break up, Boy Bye!")
   

    else:
        print("Idont understand you. Do you mind asking another question?")
