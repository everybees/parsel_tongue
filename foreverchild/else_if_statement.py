units = int (input("Enter Unit "))
if units <= 1:
    print("No Army")
elif units > 1 and units <= 9:
    print("Few")
elif units >= 10 and units <= 49:
    print("pack")
elif units >= 50 and units <= 499:
    print("hard")
elif units >= 500 and units <= 999:
    print("swarm")
elif units >= 1000:
    print("legion")