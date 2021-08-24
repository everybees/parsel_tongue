# write a program that classifies enemies based on any of the rules
# if less than 1, no army. Upto 9, few. Up to 49, pack. Up to 499, horde
# Up to 999, swarm. 1000 and more, legion.

def army_determininig_function():
    no_of_enemies = int(input("No of enemies: "))
    if no_of_enemies < 1:
        print("No army")
    elif 1 <= no_of_enemies <= 9:
        print("Few")
    elif 10 <= no_of_enemies <= 49:
        print("Pack")
    elif 50 <= no_of_enemies <= 499:
        print("Horde")
    elif 500 <= no_of_enemies <= 999:
        print("Swarm")
    elif no_of_enemies >= 1000:
        print("Legion")


army_determininig_function()
