class Building(object):
    def __init__(self, name, cohorts):
       self.name = name
       self.cohorts=cohorts
    def __str__(self) ->str:
        return self.name + "," + self.cohorts


class Cohort(object):
    def __init__(self, name, description, natives):
       self.name = name
       self.description = description
       self.natives=natives

    def __str__(self):
        return self.name


class Native(object):
    def __init__(self, first_name, last_name, sex, native_id):
        self.first_name=first_name
        self.last_name=last_name
        self.sex=sex
        self.native_id=native_id

    def __str__(self) -> str:
        return self.first_name + " " + self.last_name