import datetime
import random


print("this is precious, what question do you want answered today?")
restaurant= ["deplace", "chicken republic", "tantalizers", "Mr. Biggs"]
church= ["St Josephs Catholic Church", "RCCG", "Living Faith"]
school = ["fehingbole grammer school", "Queens college", "yabatech", "unilag"]
richest = ["Alhaji Saheed Elon Musk", "Ola Cubana", "Shenior Man"]
while True:
    question=input()
    if "restaurant" in question:
        print("the closest restaurant to this location is", random.choice(restaurant))
    elif "church" in question:
        print("the closest church to this location is", random.choice(church))
    elif "school" in question:
        print("the closest school to this location is", random.choice(school))
    elif "date" in question:
        print(datetime.datetime.now().today())
        
    elif "richest" in question:
        print("the richest person in cohort 8 is", random.choice(richest))
    elif "break" in question:
        break
    else:
        print("you clown!!, ask a question I understand")