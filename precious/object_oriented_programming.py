class building:

    def __init__(self, building_name, address):
        self.building_name = building_name
        self.address = address
        self.cohorts = []

    def __str__(self):
        cohorts = ""
        for cohort in cohorts:
            cohorts += cohort + "\n"
        return self.building_name + "\n" + self.address + "\n" + self.cohorts


class cohorts:

    def __init__(self, cohort_name):
        self.cohort_name = cohort_name
        self.cohort_description = "SCH No   |   First Name  |   Last Name   |   Sex"
        self.natives = []

    def __str__(self):
        natives = ""
        for native in self.natives:
            natives += native + "\n"
        return self.cohort_name + "\n" + self.cohort_description + "------------------------------------------------" \
                                                                   "---------" + "\n" + self.natives


class natives:

    def __init__(self, native_id, first_name, last_name, sex):
        self.native_id = native_id
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex

    def __str__(self):
        return self.native_id + "\t\t" + "|" + self.first_name + "\t\t" + "|" + self.last_name + "\t\t" + "|" + self.sex
