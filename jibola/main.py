import first_example

def get_varialbles():
    return first_example.print_do_better() + " " + first_example.print_failure_message()



if __name__ == "__main__":
        
    native = first_example.Native("Janet", "Doe")
    native.update_name("Jackie", "Chan")
    native2 = first_example.Native("Tife", "Kim")
    cohort_eight_natives = [native, native2]


    # create a student
    # student_1 = first_example.create_a_student("John", "Doe", "john_doe@email.com", "07067076636", "male")
    # cohort_eight_natives.append(student_1)
    # student_2 = first_example.create_a_student("Jane", "Doe", "jane_doe@email.com", "07067076637", "female")
    # cohort_eight_natives.append(student_2)
    # student_3 = first_example.create_a_student("Janet", "Doe", "janet_doe@email.com", "07067076638", "female")
    # cohort_eight_natives.append(student_3)
    # student_4 = first_example.create_a_student("Johnnie", "Doe", "johnnie_doe@email.com", "07067076639", "male")
    # cohort_eight_natives.append(student_4)

    # student_1['courses'].append("java")

    # for element in cohort_eight_natives:
    #     if "java" not in element['courses']:
    #         element['courses'].append('java')

    # print(cohort_eight_natives)
