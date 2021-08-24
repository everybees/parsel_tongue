value = int(input("enter number of enemies: "))

if value < 1:
    print("no army")
elif value == 1 and value < 9:
    print("few")
elif value >= 10 and value <= 49:
    print("pack")
elif value >= 50 and value <= 499:
    print("horde")
elif value >= 500 and value <= 999:
    print("swarm")
elif value >= 1000:
    print("legion")
