class Native:
    def __init__(self, native_id, first_name, last_name, sex):
        self.native_id = native_id
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex

    def __str__(self) -> str:
        return self.native_id + " " + self.first_name + " " + self.last_name + " " + self.sex



add_natives = []


# creating individual natives
def native_method( native_id, first_name, last_name, sex):
    native = Native(native_id, first_name, last_name, sex)
    print(add_natives.append(native))


# get natives
# def get_natives():
#     print("SCN  No  |    First Name    |   Last Name   |   Sex")
#     print("===================================================")
#
#     native_id = 1
#     for native in add_natives:
#         print("SCN0" + native_id + "|   ", native.first_name, "| " + native.last_Name + "|   ", native.sex)
#         native_id += 1
