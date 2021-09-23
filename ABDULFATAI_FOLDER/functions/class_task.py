# create a class of building
# create a class of cohorts
# create a class of natives
# create an object of a building that has 4 cohorts and these cohorts have natives.
# print the builiding name, the cohorts with their name and description, not forgetting the natives in these
# cohorts with their first name, last name, and their native id(SCN1 and so on).
# we can have something like this:
# Building Name: Semicolon Village
# Cohort One Natives:
# SCN No. | First Name | Last Name | Sex
# --------------------------------------
# SCN01   | John       | Doe       | Male

class Building(object):
    def __init__(self, cohorts, building_name):
        self.cohorts = cohorts
        self.building_name = building_name
    def __str__(self) -> str:
        return self.cohorts + " " + self.building_name

    

class Cohort(object):
    def __init__(self, cohort_name, cohort_description, natives):
        self.cohort_name = cohort_name
        self.cohort_description = cohort_description
        self.natives = natives
    def __str__(self) -> str:
        return self.cohort_name     


class Native(object):
  def __init__(self, first_name, last_name, sex, native_id):
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex
        self.native_id = native_id


def __str__(self) -> str:
        return self.first_name + " "  + self.last_name
     