no_of_army = int(input())

if no_of_army < 1:
    print("no army")
elif no_of_army >= 1 and no_of_army <= 9:
    print("few")
elif no_of_army >= 10 and no_of_army <=49:
    print("pack")
elif no_of_army >= 50 and no_of_army <= 499:
    print("horde")
elif no_of_army >= 500 and no_of_army <=999:
    print("swarm")
else:
    print("legion")
