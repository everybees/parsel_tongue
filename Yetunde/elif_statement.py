army = int(input())

if army < 1:
    print ("no army")
elif 1 <= army <= 9:
    print ("few")
elif 10 <= army  <= 49:
    print ("pack")
elif 50 <= army <= 499:
    print ("horde")
elif 500 <= army <= 999:
    print ("swarm")
elif army >= 1000:
    print ("legion")



