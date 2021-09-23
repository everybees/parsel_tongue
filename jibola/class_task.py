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


class Building:

    def __int__(self, building_name, cohorts):
        self.building_name = building_name
        self.cohorts = cohorts


class Cohorts:
    def __init__(self, cohorts_name, cohort_description, natives):
        self.cohorts_name = cohorts_name
        self.cohort_description = cohort_description
        self.natives = natives


class Natives:
    def __init__(self, native_id, first_name, last_name, sex):
        self.native_id = native_id
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex


add_native = []


def native_method(first_name, last_name, sex, native_id=None):
    native = Natives(native_id, first_name, last_name, sex)
    add_native.append(native)


def get_natives():
    print("SCN  No |        First Name      |       Last Name")
    print("===================================================")

    count_number_of_natives = 1
    for native in add_native:
        print("SCN0"+count_number_of_natives+ + "|      ", native.cohort_native, "|       ",+ native.sex)
        count_number_of_natives += 1


def get_cohorts():
    pass
