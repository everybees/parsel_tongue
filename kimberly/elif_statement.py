no_of_armyunits =int(input())
if no_of_armyunits < 1:
    print("no army")
elif no_of_armyunits >= 1 and  no_of_armyunits <= 9:
    print("few")
elif no_of_armyunits >= 10 and no_of_armyunits <= 49:
    print("pack")
elif no_of_armyunits >= 50 and no_of_armyunits <= 499:
    print("horde")
elif no_of_armyunits >= 500 and no_of_armyunits <= 999:
    print("swarm")
else:
    print("legion")                 