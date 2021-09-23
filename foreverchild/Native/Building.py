# from Cohort import Cohort


class Building:
    def __init__ (self, building_name, cohorts):
        self.building_name = building_name
        self.cohorts = cohorts
    def __str__(self) -> str:
        return self.building_name + " " + self.Cohorts
        