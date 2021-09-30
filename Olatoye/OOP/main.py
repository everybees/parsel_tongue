from class_task import *

global natives, cohort_details


def register_natives(first_name, last_name, gender, sc_id):
    global natives

    natives = ""
    native = Native(first_name, last_name, gender, sc_id).__str__()
    natives += native + "\n"


def add_native():
    number_of_natives = 1
    while number_of_natives < 2:
        try:
            register_natives(first_name=input("Enter first name: "), last_name=input("Enter last "
                                                                                     "name: "),
                             gender=input("Enter gender: "), sc_id=("sc" + input("Enter cohort: ") +
                                                                    str(number_of_natives)))
        except ValueError:
            print("Invalid input")
        print("\n")
        number_of_natives += 1

    return natives


def add_cohort():
    global natives, cohort_details
    number_of_cohort = 1

    while number_of_cohort < 3:
        cohort_details = Cohort(cohort_number=input("Enter cohort number"), cohort_name=input("Enter cohort name"))
        Building.cohort[f"COHORT {cohort_details.cohort_number}"] = add_native()
        print("\n\n")
        number_of_cohort += 1

    return cohort_details, Building.cohort


def add_building():
    building = Building("Semicolon Africa", "312, Herbert Macaulay Way, Sabo-Yaba, Lagos")
    add_cohort()
    print(building.__str__())
    for key in building.cohort.keys():
        print("=====================================================")
        print(key)
        print("SC_ID\t\t|FIRST NAME\t\t|LAST NAME\t\t|GENDER")
        print("-----------------------------------------------------")
        for value in building.cohort[key]:
            print(value, end="")
    print("=========================================================")


add_building()
