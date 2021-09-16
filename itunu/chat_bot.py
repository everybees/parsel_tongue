# chat bot to answer a series of  questions
# question: what is the time?
# chatbox name: precious
# answer; date and time of day
# question 2: how old are you? between 1 and 50
# question 3: have you eaten? yes or no
# question 4: do you love me? yes or no
# question 5: why am i still single? one of many reason
# /**note: a = []
# for num in range(1, 100):
#     a.append(num)
#                       ----- thesame as----
#   a =  [fornum in range(1, 100)]
# or
#   for num in range(1, 100):
#       if num %2> 0:
#           append(num)
#                        ---- thesame as----
#   a =  [fornum in range(1, 100)] if num % 2>0] */


import datetime
import random

print("This is Precious. What question do you want to ask me?")

love = ["Yes, i love you","No, i dont love you", "what is love", "Love is wicked"]
age = [num for num in range(1, 100)]
eat = ["No, i haven't", "I am not hungry", "I have had breakfast", "No, i am fasting"]
relationships = ["Wow, even the god's do not know","Yes, i am single","Yes, i am in a relationship", "it is complicated" ]
occupation = ["employed", "unemployed", "student", "employed but seeking better opportunity"]
while True:
    question = input().split()
    if "time" in question:
       print("The time of the day is:", datetime.datetime.now().time())
    elif "name" in question:
       print("My name is Precious, How can i help you?")
    elif "old" in question or "age" in question:
       print("i am 20 years, How old are you?")
    elif "eat" in  question:
       print(random.choice(eat))
    elif "love" in question:
       print(random.choice(love))
    elif "single" in question:
       print(random.choice(relationship))
    elif "occupation status" in question:
        print(random.choice(occupation))
    elif "break" in question:
       print("Seems you want to break up, Boy Bye!")
       break
    else:
     print("I don't understand you. Do you mind asking another question?'")
  