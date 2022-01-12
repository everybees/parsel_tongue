import first_example

cohort_eight = []

student = {}

if __name__ == '__main__':
    native = first_example.Native('janet', 'doe')
    print(native.first_name, native.last_name)

    #print(native)
    native.update_name("jackie", "chan")
    print(native)

    # create a student
    # student_1 = first_example.create_a_student("john", "doe", "jup@umail.com", "0566", "male")
    # cohort_eight.append(student_1)
    # student_2 = first_example.create_a_student("saheed", "tola", "jup@umail.com", "0566", "male")
    # cohort_eight.append(student_2)
    # student_3 = first_example.create_a_student("emmanuel", "olu", "jup@umail.com", "0566", "male")
    # cohort_eight.append(student_3)
    # student_4 = first_example.create_a_student("toye", "dara", "jup@umail.com", "0566", "male")
    # cohort_eight.append(student_4)
    #
    #
    # cohort_eight.append(student_1)
    #
    # student_1['courses'].append('java')
    #
    # for element in cohort_eight:
    #     if 'java' not in element['courses']:
    #         element['courses'].append('java')
    # print(cohort_eight)
