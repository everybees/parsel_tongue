army = int(input("Enter the number of armies\n"))
if army < 1:
    print("No army")
elif  1 <= army <= 9:
    print("Few")
elif 10 <= army <= 49:
    print("pack")
elif 50 <= army <= 499:
    print("Horde")
elif 500 <= army <= 999:
    print("Swarm")
elif army > 1000:
    print("Legion")
