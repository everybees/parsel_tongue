import datetime


class Building:
    def __init__(self, name, description, cohorts):
        self.name = name
        self.description = description
        self.cohorts = cohorts
        self.date_created = datetime.datetime.now()

    def __str__(self) -> str:
        return self.name

    class Cohort:
        def __init__(self, name, description, native):
            self.name = name
            self.description = description
            self.native = native
            self.date_created = datetime.datetime.now()

        def __str__(self) -> str:
            return self.name

    class Native:
        def __init__(self, scn, first_name, last_name, sex):
            self.scn= scn
            self.first_name = first_name
            self.last_name = last_name
            self.sex = sex
            self.date_created = datetime.datetime.now()
            
            
        def __valideate_native_first_name(self, first_name):
            if len(first_name) > 20:
                return ValueError("The first name has exceeded 20 charaters")
            return first_name  
        
        def __validate_native_last_name(self, last_name):
            if len(last_name) > 20:
                return ValueError("The last name has exceeded 20 charaters")
            return last_name
        
        def __validate_native_sex(self, first_name, last_name, sex):
            while True:
                try:
                    if sex.lower() == "female" or sex.lower() == "male":
                        sex = sex
                    native = Native(scn, first_name, last_name, sex)
                    return native
                except ValueError:
                    sex = input("enter valid sex: ")
        

        def __init__(self) -> str:
            return self.first_name + " " + self.last_name