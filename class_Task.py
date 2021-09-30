class Building:
    def __init__(self, building_name,cohorts):
        self.bulding_name = building_name
        self.cohorts = cohorts


class Cohorts:
    def __init__(self, cohort_names, cohort_description, natives):
        self.cohorts_names = cohort_names
        self.cohort_description = cohort_description
        self.natives = natives

    def __str__(self) -> str:
        return self.cohorts + " " + self.cohorts_description + " " +self.natives


class Natives:
    def __init__(self, scn_no, first_name, last_name, sex):
        self.scn_no = scn_no
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex

    def __str__(self) -> str:
        return self.first_name + " " + self.last_name

