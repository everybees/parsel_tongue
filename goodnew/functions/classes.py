import driver
class Native:
    def __init__(self, first_name, last_name, phone_number, sex):
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex
        self.phone_number = phone_number
        self.courses = []
    
    #     this is the to string method in python
    def __str__(self) -> str:
        return self.first_name + " " + self.last_name
    
    def set_name(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    
    native_database = []
    
    def register_native_to_cohort(first_name, last_name):
        native = Native(first_name, last_name)
        #native_database.append[native]