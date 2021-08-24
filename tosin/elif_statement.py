number = int(input("Number of enemies: "))
if number < 1:
    print("no army")
elif number >= 1 and number <=9:
    print("few") 
elif number >= 10 and number <=49:
    print("pack")
elif number >= 50 and number <=499:
    print("horde")
elif number >= 500 and number <=999:
    print("swarm")
elif number >= 1000:
    print("legion")    