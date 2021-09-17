class Native(object):
    def __init__(self, first_name, last_name, email, phone_number, sex, next_of_kin):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.sex = sex
        self.courses = []
        self.next_of_kin = next_of_kin

    def __str__(self) -> str:
        return self.first_name + " "  + self.last_name
         
    def create_next_of_kin(first_name, last_name, phone_number, sex, relationship):
        next_of_kin = N()    



    cohort_eight = []

    def register_native_to_cohort(first_name, last_name, sex, email, phone_number):
        native = Native(first_name, last_name, email, phone_number, sex)        
        cohort_eight.append(native.__str__)


class NextOfKin(object):
    def __init__(self, first_name, last_name, phone_nmuber, sex, relationship):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_nmuber
        self.sex = sex
        self.relationship = relationship       