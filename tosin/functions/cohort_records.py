class Building:
    def __init__(self, building_name, address):
        self.building_name = building_name
        self.address = address
        self.cohorts = []

    def __str__(self) -> str:
        cohorts = ""
        for cohort in self.cohorts:
            cohorts += cohort +"\n"
        return "\n\n"+"NAME OF BUILDING: " + self.building_name + "\n" +"ADDRESS: " + self.address + "\n\n" + cohorts

    # @property
    # def building_name(self):
    #     return self.building_name

    # @property
    # def address(self):
    #     return self.address

    # @property
    # def cohorts(self):
    #     return self.cohorts

    # @building_name.setter
    # def building_name(self, building_name):
    #     if len(building_name) > 100:
    #         raise ValueError("Name cannot exceed 30 characters")
    #     self.building_name = building_name

    # @address.setter
    # def address(self, address):
    #     if len(address) > 100:
    #        raise ValueError("Address cannot exceed 100 characters")
           
    # @cohorts.setter
    # def cohorts(self, cohorts):
    #     if type(cohorts) is not list:
    #         raise ValueError("List is expected")
    
class Cohort:
    def __init__(self, cohort_name):
        self.cohort_name = cohort_name
        self.cohort_natives = []
    def __str__(self) -> str:
        natives = ""
        for native in self.cohort_natives:
            natives += native + "\n"
        return "NAME OF COHORT: " + self.cohort_name + "\n\n" + "SCN No. | First Name    | Last Name     | Sex" + "\n" + "----------------------------------------------" + " \n" +natives

    # @property
    # def cohort_name(self):
    #     return self.cohort_name

    # @property
    # def cohort_natives(self):
    #     return self.cohort_natives

    # @cohort_natives.setter
    # def cohort_natives(self, cohort_natives):
    #     if type(cohort_natives) is not list:
    #         raise ValueError("list of natives is required")
    #     self.cohort_natives = cohort_natives
    # @cohort_name.setter
    # def cohort_name(self, cohort_name):
    #     if len(cohort_name) > 30:
    #         raise ValueError("Name cannot execeed 30 characters")
    #     self.cohort_name = cohort_name


class Native:
    def __init__(self, sc_id, first_name, last_name, sex):
        self.sc_id = sc_id
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex
        
    def __str__(self) -> str:
        return self.sc_id + "\t|"  + self.first_name + "\t\t|" + self.last_name + "\t\t|" + self.sex 

    # @property
    # def sc_id(self):
    #     return self.sc_id
    # @property
    # def first_name(self):
    #     return self.first_name
    # @property
    # def last_name(self):
    #     return self.last_name
    # @property
    # def sex(self):
    #     return self.sex
    # @sc_id.setter
    # def sc_id(self, sc_id):
    #     if len(sc_id) > 10:
    #         raise ValueError("Character cannot exceed 10")
    #     self.sc_id = sc_id
    # @first_name.setter
    # def first_name(self, first_name):
    #     if len(first_name) > 20:
    #         raise ValueError("Character cannot exceed 20")
    #     self.first_name = first_name
        
    # @last_name.setter
    # def last_name(self, last_name):
    #     if len(last_name) > 20:
    #         raise ValueError("Character cannot exceed 20")
    #     self.last_name = last_name
    # @sex.setter
    # def sex(self, sex):
    #     sex = sex.islower()
    #     if sex != "male" and sex != "female":
    #         raise ValueError("Enter valid gender")
    #     self.sex = sex