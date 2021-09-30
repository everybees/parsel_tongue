from dami_cohort import Building
from dami_cohort import Native
from dami_cohort import Cohort
#   dami_cohort
if __name__ =="__main__":
    print("Good day, I am here to make your life better")
    building_name = input("Enter your Building's name: ")
    building_address = input("Enter your building's address: ")
    main_building = Building(building_name, building_address)
    
    number_of_cohorts = int(input("How many Cohorts Would You Like to Add: "))

    for n in range(0, number_of_cohorts):
        cohort_name = input("Enter cohort name: ")
        cohort = Cohort(cohort_name)

        number_of_natives = int(input("How many natives do you want to admit to this cohort: "))
        for r in range(0, number_of_natives):
            native_id = input("Enter natives id: ")
            native_first_name = input("Enter natives first name: ")
            native_last_name = input("Enter natives last name: ")
            native_sex = input("Enter natives gender: ")

            native = Native(native_id, native_first_name, native_last_name, native_sex)

            cohort.cohort_natives.append(native.__str__())
        
        main_building.cohorts.append(cohort.__str__())


    print(main_building)
  
