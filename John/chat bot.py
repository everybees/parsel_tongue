import datetime
import random
# we use .split() to make input in list
# is check the type, in check the value
question = input().split()
age = [num for num in range(1,100)]
relationships = ["wow, even the gods do not know.", "yes i am single", "yes, i am in a relationship", "it is complicated"]
eat = ["No i have not eaten", "Yes i have eaten", "yes i ate eba and egusi soup", "no I am fasting" ]
love = ["yes I love you!", "no I dont love you", "What is love", "Love is wicked"]
colour = ["black", " white", " red", "orange", "yellow", "pink"]
church = ["MFM church", "redeem church", "Gospel church", "deeper life Bible church", "church of God"]
friend = ["ade", "Gideon", "Bolu", "Femi", "Yetunde"]
bank = ["first bank", "GTbank", "Access bank", "kuda bank"]

while True:
 if "time" in question:
    print ("the time of day is: ", datetime.datetime.now().time())
 elif "name" in question:
    print("my name is Precious, How can I help you ")
 elif "old" in question or age in question:
     
    print("I am ", random.choice(age),  "years, How old are ")
 elif "eat" in question or "eaten":
    print(random.choice(eat))
 elif "single" in question:
    print(random.choice(relationships))

# to make random selection use random.choice() 
# append.() is use to add to a list 
 elif "love" in question:
    print("I am", random.choice(love), "years old")
 elif "favourite colour" in question:
     print (random.choice(colour))
 elif "church" in question:
     print(random.choice(churcch))
 elif "friend" in question:
     print(random.choice(friend))
 elif "bank" in question:
     print(random.choice(bank))
 else:
    print("I dont understand you. do you mean the time of the day?")

