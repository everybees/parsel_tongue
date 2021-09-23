from Olatoye.functions import exercise


def user_details(counter):
    user_dictionary = {
        "id": "user" + str(counter),
        "first_name": input("Enter first name: "),
        "last_name": input("Enter last name: "),
        "email": input("Enter email address: "),
        "password": input("Enter password: ")
    }

    return user_dictionary


def enter_user_details():
    list_of_users = []
    counter = 1
    while True:
        list_of_users.append(user_details(counter))
        counter += 1
        if counter == 3:
            break


enter_user_details()
