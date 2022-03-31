import assignment
import building_records
from building_records import Building, Cohort, Native
if __name__ == "__main__":
    global_container = []
    number_of_building = int(input("How many buildings do you want to generate: "))
    for i in range(number_of_building):
        name_of_building = input("Enter the name for building " + str(i+1) + ": ")
        description = input("Enter the address for " + name_of_building + ": ")
        building = Building(name_of_building, description)
        number_of_cohorts = int(input("Enter the number of cohorts in " + name_of_building + ": "))
        for i in range(number_of_cohorts):
            name_of_cohort = input("Enter name for cohort "+ str(i+1)+ ": " )
            cohort = Cohort(name_of_cohort)
            number_of_natives = int(input("Enter the number of natives in " + name_of_cohort + ": "))
            for i in range(number_of_natives):
                id_number = input("Enter id number for native " + str(i+1) + " in " + name_of_cohort +": ")
                first_name = input("Enter the firstname: ")
                last_name = input("Enter the lastname: ")
                gender = input("Enter gender type: ")
                native = Native(id_number, first_name, last_name, gender)
                cohort.cohort_natives.append(native.__str__())
            building.cohorts.append(cohort.__str__())
        global_container.append(building.__str__())

    for building in global_container:
        print(building)