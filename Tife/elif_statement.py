enemy = int(input("Enter number of enemies: "))

if enemy<1:
    print("no army")
elif enemy == 1 and enemy <= 9:
    print("few")
elif enemy >= 10 and enemy < 50:
    print("pack")
elif enemy >= 50 and enemy <= 499:
    print("horde")
elif enemy >= 500 and enemy <= 999:
    print("swarm")                
elif enemy > 999:
    print("legion")
#else: print("Your enemies have been defeated")