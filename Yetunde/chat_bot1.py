import random

print('This is becky. how may i help you?')

dictionary = {"ingredients": ["Flour", "Sugar", "Baking powder", "Milk", "Preservative"],
            "inches": ["5 inches", "7 inches", "8 inches", "10 inches", "12 inches"],
            "flavor": ["Chocolate", "Vanilla", "Strawberry", "Red velvet"],
            "order": ["Cake", "Chinchin", "Doughnut", "Burger", "Small chops", "Meat pie"],
            "event":  ["Birthday", "Wedding", "Bridal shower", "Baby shower"],
            "gender": ["Male", "Female"], 
}

while True:
    order = input().split()
    if ["exit"] == order:
        print("Thanks for your patronage")
        break
    options = []

    for key in dictionary:
        if key in order:
            options.append(random.choice(dictionary[key]))
    if options:
        print(random.choice(options))
            
    else:
         print("I don't understand. Ask me something else")
   

