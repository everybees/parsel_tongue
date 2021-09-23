from class_task import *


Cohort.natives = []


def register_natives(first_name, last_name, gender, sc_id):
    native = Native(first_name, last_name, gender, sc_id)
    Cohort.natives.append(native)


def add_native():
    number_of_natives = 1

    while number_of_natives < 2:
        register_natives(first_name=input("Enter first name: "), last_name=input("Enter last "
                                                                                 "name: "),
                         gender=input("Enter gender: "), sc_id=("sc" + input("Enter cohort: ") +
                                                                str(number_of_natives)))
        print("\n")
        number_of_natives += 1
    # for native in natives:
    #     print(native)
    return Cohort.natives


Building.cohort = {}


def add_cohort():
    number_of_cohort = 1

    while number_of_cohort < 2:
        cohort_details = Cohort(cohort_number=input("Enter cohort number"), cohort_name=input("Enter cohort name"))
        # cohort_natives = add_native()
        Building.cohort["Cohort {0}".format(str(number_of_cohort))] = add_native()
        print("\n\n")
        number_of_cohort += 1

    return Building.cohort


def add_building():
    building = Building("Semicolon Africa")
    add_cohort()
    print(Building.__str__())


add_building()
