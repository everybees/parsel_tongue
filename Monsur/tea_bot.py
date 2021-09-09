
dictionary = {
    "tea": ["pay 500 Naira to the cashier and grab your drink"],
    "coffee": ["pay 500 Naira to the cashier and grab your drink"],
    "why": ["Never mind!"]
    }
print("HI, my name is Solibot, we only sell coffee and tea else write none to exit: ")
while True:
    user = input().split()

    for keys, value in dictionary.items():
        if keys in user:
            print(random.choice(value))
            print("make another request")
            break
        if user == "exit":
            print("exiting...")
            break
    else:
        print("Wrong choice, you can only choose tea or coffee: ")









