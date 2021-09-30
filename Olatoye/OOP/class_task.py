class Native:
    def __init__(self, first_name, last_name, gender, sc_id):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.sc_id = sc_id

    # @property
    # def first_name(self):
    #     return self.first_name
    #
    # @property
    # def last_name(self):
    #     return self.last_name
    #
    # @property
    # def gender(self):
    #     return self.gender
    #
    # @first_name.setter
    # def first_name(self, value):
    #     if len(value) > 20:
    #         raise ValueError("Name cannot exceed 20 characters")
    #     self.first_name = value
    #
    # @last_name.setter
    # def last_name(self, value):
    #     if len(value) > 20:
    #         raise ValueError("Name cannot exceed 20 characters")
    #     self.last_name = value
    #
    # @gender.setter
    # def gender(self, value):
    #     if value != "female" and value != "male" and value != "other":
    #         raise ValueError("Invalid gender")
    #     self.gender = value

    # def __str__(self):
    #     return str(self.sc_id) + "\t\t|" + self.first_name + "\t\t|" + self.last_name + "\t\t|" + self.gender

    def __str__(self):
        return self.first_name, self.last_name + self.gender + self.sc_id


class Cohort:
    natives_dict = {}

    def __init__(self, cohort_number, cohort_name):
        self.cohort_number = cohort_number
        self.cohort_name = cohort_name

    def __str__(self):
        return self.cohort_number + "\t" + self.cohort_name + "\n"


class Building:
    cohort_dict = {}

    def __init__(self, building_name, building_address):
        self.building_name = building_name
        self.building_address = building_address

    def __str__(self):
        return self.building_name + "\n" + self.building_address + "\n"

