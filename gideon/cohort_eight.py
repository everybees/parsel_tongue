def create_student(first_name, last_name, email, phone_number, sex):
    student = {}
    student["first_name"] = first_name
    student["last_name"] = last_name
    student["email"] = email
    student["phone_number"] = phone_number
    student["sex"] = sex
    student["courses"] = []

    return student

# class Native():
#     first_name = "Jane"
#     last_name = "Mena"

# class Nativer:
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.first_name = last_name
#         self.courses = []
