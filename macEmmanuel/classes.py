# classes

class Native:
    def __init__(self, first_name, last_name, phone_number):  # Constructor
        self.first_name = first_name,
        self.last_name = last_name,
        self.love = True;

        # This is a toString function in Python like Java

    def __str__(self) -> str:
        return self.first_name + " " + self.last_name + " " + self.sex

    def set_phone_number(self, phone_number):
        self.phone_number = phone_number

    def set_sex(self, sex):
        self.sex = sex

    def set_name(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

        # student = Native(student):     #Creating Object of Class Native
        # print(self.love)

        Native.set_name()
