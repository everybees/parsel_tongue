import random
import datetime

print("Lets figure how to make it work out in our furniture business")


furniture = {
        "staffs" : ["Secretary", "GateMen", "Cleaners", "Manager", "Director", "Labourer"],
        "source" : ["Forest", "Raw Materials", "Tools"],
        "salary" :  ["Monthly", "Weekly", "Daily"],
        "age" : ["from 18years", "To your strength"],
        "duration" : ["Contract", "Full Staff"]
    }

while True:
    question = input().split("_")
    for fun in question:
        if fun in furniture.keys():
            print(random.choice(furniture[fun]))
            break
    else:
        print("More ideas are welcome")
