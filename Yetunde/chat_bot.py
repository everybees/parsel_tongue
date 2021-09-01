# chat bot to answer series of questions 
# questions: what is the time of the day?

import datetime
import random

print("This is presh. How may I help you?")

love = ["Yes, I love you", "No, I don't love you", "love is wicked", "What is love"]
age = [num for num in range(1, 100)]
eat = ["No, I haven't", " Yeah , I have had breakfast", "Yes I am single"] 
color = ["Blue", "Green", "Yellow", "White", "Red", "Violet", "Magenta", "pink"]
cake = ["Chocolate", "Red velvet", "Vanilla", "Strawberry", "Dessert Cake", "Marble Cake"]
country = ["United States", "Canada", "France", "Germany", "Australia", "Ghana", "South Africa", "Nigeria"]
food = ["Chicken and chips", "Sharwama", "Jollof rice", "Yam and egg", "Amala and ewedu", "Indomie"]

while True:
    question = input()
    if "time" in question:
         print("The time of the day is:", datetime.datetime.now().time())
    elif "name" in question:
         print ("My name is Precious, How may i help you?")
    elif "old" in question or "age" in question:
        print ("I am", random.choice(age), "years old")
    elif "eat" in question or "eaten" in question:
        print("Yes, I have eaten.")
    elif "love" in question:
        print (random.choice(love))
    elif "color" in question:
        print ("My best color is ",random.choice(color))
    elif "cake" in question:
        print ("I love",random.choice(cake))
    elif "country" in question:
        print ("I would like to visit",random.choice(country))
    elif "food" in question:
        print (random.choice(food))
    elif "break" in question:
        print ("Seems you want to break up, Bye!")
        break
    else:
     print(" I don't understand. Do you mind asking another question")