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

print("This is candy.What question do you want answered today?")

keyword = {
  "love" : ["Yes,I love you!","No,I dont love you","what is love?","love is wicked"],
  "age" : [num for num in range(1,100)],
  'eat' : ["No, I havent","Yeah,I have had breakfast","Yeah, I had eba and egusi", "No, I am fasting."],
  "nigeria" : ["omo!!!! you gats japa", "You still dey this country?" "well well!! what can i say change your president"],
  "damilola" :["I love her","Ever met someone so perfect?", "She hates negativity", "That name is just as perfect as the owner"],
  "bored" : ["play games","go and chill", "you need friends","you have me"],
  "friend" : ["we'll always be friends", "No learn to be independent", "everybody likes you","You are still my friend"],
  "happy" :["It is a thing of the mind", "Its a good thing to feel but let your feelings not cloud your judgement", "always smile","I'm proud of you"],
  "exit": []
  }

while True:
  question = input().split()
  if ["exit"] == question:
      print("Exiting.....")
      break
   
  for word in question:
    if word in keyword.keys():
      print(random.choice(keyword[word]))
      break

  else:
      print("Ask another question")

  
   