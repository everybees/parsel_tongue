class Building:
    def __init__(self, name, cohorts):
        self.name = name
        self.cohorts = cohorts

    def __str__(self):
        return self.name + "," + self.cohorts

    def _building_name(self, building_name):
        if len(building_name) > 20:
            raise ValueError("Building name is too long.")
        if type(building_name) is not str:
            raise ValueError("Input is not applicable here.")
        return building_name


class Cohorts:
    def __init__(self, cohort_name, natives, description):
        self.cohort_name = cohort_name
        self.cohort_description = description
        self.natives = natives

    def __str__(self):
        return self.cohort_name

    def _check_cohorts(self, cohort):
        if type(cohort) is not list:
            raise ValueError("Invalid cohort type.")
        return cohort


class Native:
    def __init__(self, first_name, last_name, native_id, sex):
        self.first_name = first_name
        self.last_name = last_name
        self.native_id = native_id
        self.sex = sex

    def __str__(self):
        return self.first_name + " " + self.last_name

    # def check_native_input(self, native):
