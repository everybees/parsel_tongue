class Building:
    def __init__(self, building_name, cohort):
        self.building_name = building_name
        self.cohort = cohort

    def __str__(self) -> str:
        return self.name


class Cohorts:
    def __init__(self, name, description, native):
        self.name = name
        self.description = description
        self.native = native

    def __str__(self) -> str:
        return self.name + " " + self.description


class Natives:
    def __init__(self, first_name, last_name, nativeID, sex):
        self.first_name = first_name
        self.last_name = last_name
        self.nativeID = nativeID
        self.sex = sex

    def __str__(self) -> str:
        return self.first_name + " " + self.last_name

