"""

create a class of building
create a class of cohorts
create a class of natives

create an object of a building that has 4 cohorts and these cohorts have natives.

print the builiding name, the cohorts with their name and description, not forgetting the natives in these
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
    def __int__(self, building_name, get_cohorts):
        self.building_name = building_name
        self.get_cohorts = get_cohorts


class Cohort:
    def __init__(self, cohort_name, cohort_description, natives):
        self.cohort_name = cohort_name
        self.cohort_description = cohort_description
        self.natives = natives

    def __str__(self) -> str:
        return self.cohort_name + " " + self.cohort_description + " "


add_cohorts = []


def cohorts_method(cohort_name, cohort_description, natives):
    cohort = Cohort(cohort_name, cohort_description, natives)
    add_cohorts.append(cohort)


def get_cohorts():
    count_number_of_cohorts = 1
    for cohort in add_cohorts:
        print(cohort.cohort_name, cohort.cohort_description)
        count_number_of_cohorts += 1


class Native:
    def __init__(self, native_id, first_name, last_name, sex):
        self.native_id = native_id
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex

    def __str__(self) -> str:
        return self.native_id + " " + self.first_name + " " + self.last_name + " " + self.sex


add_natives = []


def native_method(native_id, first_name, last_name, sex):
    native = Native(native_id, first_name, last_name, sex)
    add_natives.append(native)
    return native


# get natives
def get_natives():
    print("SCN  No  |    First Name    |   Last Name   |   Sex")
    print("===================================================")
    native_method()

    count_number_of_natives = 1
    for native in add_natives:
        print("SCN0" + count_number_of_natives + "|   ", native.first_name, "| " + native.last_Name + "|   ", native.sex)
        count_number_of_natives += 1
