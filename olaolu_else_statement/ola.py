number_of_army = int(input("Enter number:"))
if number_of_army < 1:
    print("No Army")

elif number_of_army >= 1 <= 9:
    print("few")

elif number_of_army >= 10 <= 49:
     print("pack")

elif number_of_army >= 50 <= 499:
    print("hord")

elif number_of_army >= 500 <= 999:
    print("swarm")

else:
    print("Legion")

