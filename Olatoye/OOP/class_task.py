"""

create a class of building
create a class of cohorts
create a class of natives

create an object of a building that has 4 cohorts and these cohorts have natives.

print the building name, the cohorts with their name and description, not forgetting the natives in these
cohorts with their first name, last name, and their native id(SCN1 and so on).

we can have something like this:

Building Name: Semicolon Village

Cohort One Natives:
SCN No. | First Name | Last Name | Sex
--------------------------------------
SCN01   | John       | Doe       | Male
....


"""


class Native:
    def __init__(self, first_name, last_name, gender, sc_id):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.sc_id = sc_id

    def __str__(self):
        return str(self.sc_id) + " " + self.first_name + " " + self.last_name + " " + self.gender


natives = []


def register_natives(first_name, last_name, gender, sc_id):
    native = Native(first_name, last_name, gender, sc_id)
    natives.append(native)


class Cohort:
    def __init__(self, cohort_number, cohort_name):
        self.cohort_number = cohort_number
        self.cohort_name = cohort_name

    def __str__(self):
        return self.cohort_number + " " + self.cohort_name


cohort = {}


class Building:
    def __init__(self, building_name):
        self.building_name = building_name

    def __str__(self):
        return self.building_name


def add_native():
    number_of_natives = 1

    while number_of_natives < 3:
        register_natives(first_name=input("Enter first name: "), last_name=input("Enter last "
                                                                                 "name: "),
                         gender=input("Enter gender: "), sc_id=("sc" + input("Enter cohort: ") +
                                                                str(number_of_natives)))
        number_of_natives += 1
    # for native in natives:
    #     print(native)


add_native()
