

class Building:
    def __init__(self, cohort):
        self.cohort = cohort



class Cohort:
    def __init__(self, native, name_of_the_cohort):
        self.native = native
        self.name_of_the_cohort = name_of_the_cohort
    def __str__(self) -> str:
        return self.name_of_the_cohort
class Native:
    def __init__(self, first_name, last_name, email, password, phonenumber, sex ):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.passwoord = password
        self.phonenumber = phonenumber
        self.sex = sex
        
    def __str__(self) -> str:
        return self.first_name + " " + self.last_name 
native_of_cohort = []   

def register_native_to_cohort(first_name, last_name, email, password,  phone_number, sex):
     native = Native(first_name, last_name, email, password,  phone_number, sex)
     native_of_cohort.append(native.__str__())
cohort_of_building = []
def register_cohort_to_building(native, name_of_cohort):
    cohort = Cohort(native, name_of_cohort)
    cohort_of_building.append(cohort.__str__())
