from object_oriented_programming import Native


def create_natives(scn, first_name, last_name, sex):
    while True:
        try:
            if sex.lower() == "female" or sex.lower() == "male":
                sex = sex
            native = Native(scn, first_name, last_name, sex)
            return native
        except ValueError:
            sex = input("enter valid sex: ")
