class Building:
    def __init__(self, name):
        self.name = name
        self.cohorts = []

    def __str__(self):
        return self.name


class Cohorts:
    def __init__(self, cohort_name):
        self.cohort_name = cohort_name
        self.cohort_description = ""
        self.natives = []

    def __str__(self):
        return self.cohort_name


class Natives:
    def __init__(self, first_name, last_name, native_id, sex):
        self.first_name = first_name
        self.last_name = last_name
        self.native_id = native_id
        self.educational_status = sex

    def __str__(self):
        return self.native_id