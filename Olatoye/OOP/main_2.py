from class_task import *


def add_native():
    native_dict = {}
    native_ = Native(input("Enter Native's first name"), input("Enter Native's last name"),
                     input("Enter Native's gender"), input("Enter Native's sc_id"))
    native_dict["First Name"] = native_.first_name
    native_dict["Last Name"] = native_.last_name
    native_dict["Gender"] = native_.gender
    native_dict["SC ID"] = native_.sc_id

    return native_dict


def add_natives(number_of_natives):
    dict_of_natives = {}
    while number_of_natives != 0:
        dict_of_natives[f"Native {number_of_natives}"] = add_native()
        number_of_natives -= 1
    return dict_of_natives


def add_cohort(cohort_number_):
    cohort_ = Cohort(cohort_number_, input("Enter Cohort name"))
    number_of_natives = input("Enter number of natives")
    cohort_.natives_dict[f"Cohort {cohort_number_} ({cohort_.cohort_name})"] = add_natives(number_of_natives)
    return cohort_.natives_dict


def add_cohorts(number_of_cohorts):
    dict_of_cohorts = {}
    while number_of_cohorts != 0:
        cohort_number_ = input('Enter Cohort Number')
        dict_of_cohorts[f"Cohort {cohort_number_}"] = add_cohort(cohort_number_)
        number_of_cohorts -= 1
    return dict_of_cohorts


def add_building():
    building_ = Building(input("Enter Building name"), input("Enter Building address"))
    number_of_cohorts = input("Enter number of cohorts")
    building_.cohort_dict[f"Building {number_of_cohorts}"] = add_cohorts(number_of_cohorts)
    return building_.cohort_dict


def add_buildings(number_of_buildings_):
    dict_of_buildings = {}
    while number_of_buildings_ != 0:
        dict_of_buildings[f"Building {number_of_buildings_}"] = add_building()
        number_of_buildings_ -= 1
    return dict_of_buildings


if __name__ == "__main__":

    number_of_buildings = input("Enter number of buildings")
    buildings = add_buildings(number_of_buildings)

    for building_number in buildings.keys():
        print(building_number)
        for building in buildings.values():
            for cohort_number in building.keys():
                print(cohort_number)
                for cohort in building.values():
                    for native in cohort.values():
                        print(native)

    # for key in run.keys():
    #     print(key)
    #     for value in run.values():
    #         for value_ in value.values():
    #             for value__ in value_.values():
    #                 print(value__, end="  ")
