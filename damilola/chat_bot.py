#chatbot to answer a series of questions

#question: what is the time;
#chatbot: Precious

#question 1: what is the time? current time
#question 2: how old are you? between 1 and 50
#question 3:have you eaten? yes or no
#question 4: do you love me? yes or no
#question 5: why am i still single? one of many reasons
#question 6: Why is Nigeria not getting better? one of many reasons
# queston 7: What do you think about damilola? one of many reasons
#question 8:Do you ever feel bored? yes or no
# question 9: Do you have friends? yes or no
#question 10:Are you happy? yes or no


import datetime
import random

print("This is precious.What question do you want answered today?")


love = ["Yes,I love you!","No,I dont love you","what is love?","love is wicked"]
age = [num for num in range(1,100)]
eat = ["No, I havent","Yeah,I have had breakfast","Yeah, I had eba and egusi", "No, I am fasting."]
relationships = ["Wow,even the gods do not know.","Yes, i am single", "Yes,I am in a relationship","Its complicated"]
nigeria = ["omo!!!! you gats japa", "You still dey this country?" "well well!! what can i say change your president"]
damilola = ["I love her","Ever met someone so perfect?", "She hates negativity", "That name is just as perfect as the owner"]
bored = ["play games","go and chill", "you need friends","you have me"]
friend = ["we'll always be friends", "No learn to be independent", "everybody likes you","You are still my friend"]
happy = ["It is a thing of the mind", "Its a good thing to feel but let your feelings not cloud your judgement", "always smile","I'm proud of you"]
while True:
  question = input()
  if "time" in question:
    print("The time of day is:",datetime.datatime.now ().time())
  elif "name" in question:
    print("My name is precious,How can i help you?")
  elif "old" in question or "age" in question:
    print("I am",random.choice(age)) ,"years old"
  elif "eat" in question or "eaten" in question:
    print(random.choice(eat))
  elif "love" in question:
    print(random.choice(love))
  elif "single" in question or 'relationship' in question:
    print(random.choice(relationships))
  elif "break" in question:
    print("Seems you want to break up,Boy Bye!")
    break
  elif "nigeria" in question:
    print(random.choice(nigeria))
  elif "damilola" in question:
    print(random.choice(damilola))
  elif "bored" in question or "boring" in question:
    print(random.choice(bored))
  elif "friend" in question or "friends" in question:
    print(random.choice(friend))
  elif "happy" in question or "happiness" in question:
    print(random.choice(happy))
  else:
    print("I dont understand you.Do not mind asking another question?")
