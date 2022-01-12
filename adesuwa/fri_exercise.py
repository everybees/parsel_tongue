def create_a_student(first_name, last_name, email, phone_number, sex):
    student = {}
    student['first_name'] = first_name
    student['last_name'] = last_name
    student['email'] = email
    student['phone_number'] = phone_number
    student['sex'] = sex
    student['courses'] = []

    return student


class Native:
    def __init__(self, first_name, last_name, email, phone_number, sex, next_of_kin):
         self.first_name = first_name
         self.last_name = last_name
         self.sex = sex
         self.next_of_kin = next_of_kin
         self.phone_number = phone_number
         self.email = email
         self.courses = []

    def _str_(self) -> str:
        return self.first_name + " " + self.last_name


class NextOfKin:
    def __init__(self, first_name, last_name, relationship, sex, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.relationship = relationship
        self.sex = sex
        self.phone_number = phone_number
        self.rich = False

    def __str__(self) -> str:
       return self.first_name + " " + self.last_name

    next_of_kin_data = []


def create_next_of_kin(first_name, last_name, phone_number, relationship, email, sex):
    next_of_kin = NextOfKin(first_name, last_name, phone_number,relationship, email, sex)
    return next_of_kin


cohort_eight = []


def register_native_to_cohort(first_name, last_name, sex, phone_number, email):
    native = Native(first_name, last_name, email, phone_number, sex)
    cohort_eight.append(native)


def get_cohort_eight_natives():
    print("No. | first name | last name | email |")
    print("======================================")

    value = 1
    for native in cohort_eight:
        print(value, "  |", native.first_name, "  |", native.last_name, "  |", native.sex, "  |", native.email, "  |", native.phone_number)
        value += 1