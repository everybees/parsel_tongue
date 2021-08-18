user_input = input("Enter a number:")
user_input = int(user_input)
if user_input % 2 != 0:
    print("Weird")
if user_input % 2 == 0:
    if user_input >= 2 and user_input <= 5:
        print("Not Weird")
    if user_input >= 6 and user_input <= 20:
        print("Weird")
    if user_input >= 20:
        print("Not Weird")


