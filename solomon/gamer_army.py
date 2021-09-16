army = int(input("Enter your units: "))

if army < 1:
    print("No army")
elif 1 <= army <= 9:
    print("Few")
elif 10 <= army <= 49:
    print("Pack")
elif 50 <= army <= 499:
    print("Horde")
elif 500 <= army <= 999:
    print("Swarm")
else:
    print("Legion")
