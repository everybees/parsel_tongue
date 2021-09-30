class Building:
    def __init__(self, building_name, cohort):
        self.building_name = self.__building_name(building_name)
        self.cohort = cohort

    def __str__(self) -> str:
        return self.building_name

    def __building_name(self, something):
        if len(something) > 20:
            raise ValueError("name cannot exceed 20 character")
        return something


class Cohorts:
    def __init__(self, name, description, native):
        self.name = name
        self.description = description
        self.native = native

    def __str__(self) -> str:
        return self.name


class Natives:
    def __init__(self, first_name, last_name, nativeID, sex):
        self.first_name = first_name
        self.last_name = last_name
        self.nativeID = nativeID
        self.sex = sex

    def __str__(self) -> str:
        return self.first_name + " " + self.last_name

