def print_success_message():
    return "success"


def print_failure_message():
    return "failed"


def print_try_again():
    return "try again"


def print_do_better():
    return "you can do better"


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
        self.email = email
        self.phone_number = phone_number
        self.sex = sex
        self.courses = []
        self.next_of_kin = next_of_kin

    def __str__(self) -> str:
        return self.first_name + " " + self.last_name


class NextOfKin:
    def __init__(self, first_name, last_name, phone_number, sex, relationship):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.sex = sex
        self.relationship = relationship

    def __str__(self) -> str:
        return self.first_name + " " + self.last_name


def create_next_of_kin(first_name, last_name, phone_number, sex, relationship):
    next_of_kin = NextOfKin(first_name, last_name, phone_number, sex, relationship)
    return next_of_kin


cohort_eight = []


def register_native_to_cohort(first_name, last_name, sex, phone_number, email, next_of_kin):
    native = Native(first_name, last_name, email, phone_number, sex, next_of_kin)
    cohort_eight.append(native)


def get_cohort_eight_natives():
    print("No.  | first name   | last name | email |")
    print("==========================================")

    value = 1
    for native in cohort_eight:
        print(value, "  |", native.first_name, "    |", native.last_name, " |", native.email)
        value += 1
