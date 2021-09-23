user_input = int (input("enter a number "))
if user_input < 1:
    print("no army")
elif user_input >= 1 and user_input <=9:
    print("few")
elif user_input >= 10 and user_input <= 49:
    print("pack")
elif user_input >= 50 and user_input <=449:
    print("horde")
elif user_input >= 500 and user_input <=999:
    print("swarm")
elif user_input > 1000:
    print("legion")

