from class_task import *


def add_native():
    native_dict = {}

    native = Native(input("Enter Native's first name"), input("Enter Native's last name"),
                    input("Enter Native's gender"), input("Enter Native's sc_id"))

    native_dict["First Name"] = native.first_name
    native_dict["Last Name"] = native.last_name
    native_dict["Gender"] = native.gender
    native_dict["SC ID"] = native.sc_id

    return native_dict


def add_cohort():
    cohort_dict = {}

    cohort = Cohort(input("Enter Cohort number"), input("Enter Cohort name"))

    cohort_dict[f"Cohort {cohort.cohort_number} ({cohort.cohort_name})"] = add_native()

    return cohort_dict


run = add_cohort()

for key in run.keys():
    print(key)
    for value in run.values():
        for value_ in value.values():
            print(value_, end=" ")
