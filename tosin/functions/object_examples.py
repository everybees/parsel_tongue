class Native:
    def __init__(self, first_name, last_name, phone_number, email, sex, next_of_kin):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email
        self.sex = sex
        self.courses = []
        self.next_of_kin = next_of_kin
        
    def __str__(self) -> str:
        return self.first_name + " "+ self.last_name