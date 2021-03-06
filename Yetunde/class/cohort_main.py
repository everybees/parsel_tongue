from typing import no_type_check_decorator
import cohort_natives
from cohort_natives import Cohort
from cohort_natives import Building
from cohort_natives import Native

if __name__ == "__main__":
    building_name = input("Enter Building's name: ")
    main_building = Building(building_name, building_address)

    number_of_cohorts = int(input("How many Cohorts do you want to create in your building: "))

    for n in range(0, number_of_cohorts):
        cohort_name = input("Enter cohort name: ")
        cohort_description = input("Enter cohort description: ")
        native = []
        cohort = Cohort(cohort_name, cohort_description, native)

        number_of_natives = int(input("How many natives do you want to admit to each cohort: "))
        for r in range(0, number_of_natives):
            native_id = input("Enter natives id: ")
            native_first_name = input("Enter natives first name: ")
            native_last_name = input("Enter natives last name: ")
            native_sex = input("Enter natives gender: ")

            native = Native(native_id, native_first_name, native_last_name, native_sex)

            Cohort.cohort_natives.append(native.__str__())

            main_building.cohorts.append(cohort.__str__())


    print(main_building)