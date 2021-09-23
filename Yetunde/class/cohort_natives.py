
class Building:
    def __init__(self, building_name, cohorts):
        self.building_name = building_name
        self.cohorts = cohorts
    
    def __str__(self) -> str:
        return self.building_name + ': ' + self.cohorts      
        
        
class Cohort:
    def __init__(self, cohort_name, cohort_description, natives):
        self.cohort_name = cohort_name
        self.cohort_description = cohort_description
        self.natives = natives
        
    def __str__(self) -> str:
        return self.cohort_name + " " + self.cohort_description    
            
class Native:
    def __init__(self, first_name, last_name, sex, id ):
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex
        self.id = id
        
    def __str__(self) -> str:
        return self.first_name + " " + self.last_name