class Building:
    def __init__(self, name, cohorts):
        self.name = name
        self.cohorts = cohorts

    def __str__(self):
        return self.name + "," + self.cohorts


class Cohorts:
    def __init__(self, cohort_name, natives, description):
        self.cohort_name = cohort_name
        self.cohort_description = description
        self.natives = natives

    def __str__(self):
        return self.cohort_name


class Native:
    def __init__(self, first_name, last_name, native_id, sex):
        self.first_name = first_name
        self.last_name = last_name
        self.native_id = native_id
        self.sex = sex

    def __str__(self):
        return self.first_name + " " + self.last_name