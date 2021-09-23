from ABDULFATAI_FOLDER.functions.class_task import Building, Cohort
import class_task

if __name__ == "__main__":


    natives1 = []
    natives2 = []
    natives3 = []

    cohorts = []
    natives1 = class_task.Native("Jane", "Doe", "F", "SCN01")
    natives1.append(natives1)
    natives2 = class_task.Native("Johnny", "Doe", "M", "SCN02")
    natives2.append(natives2)
    natives3 = class_task.Native("James", "Bond", "M", "SCN03")
    natives3.append(natives3)

    new_cohort = class_task.Cohort("cohort_one", "Short and dark skin", natives1)
    cohorts.append(new_cohort)
    new_cohort = class_task.Cohort("cohort_two", "Fat and dark skin", natives2)
    cohorts.append(new_cohort)
    Building = class_task.Building(cohorts, "Semicolon Village")
    print(Building.building_name)

    for cohort in Building.cohorts:
        if cohort.cohort_name =="cohort_one":
            print(cohort.cohort_name + ":")
            print("SCN NO.|   First name   |   Last name   |  sex")
            for native in cohort.natives:
                print(native.native_id + "    |" + native.first_name + "    |" + native.last_name + "    |" + native.sex)
                print("\n==============================================================================================")

        else:
            print(cohort.cohort_name + ":")   
            for native in cohort.natives:
                print(native.native_id + "    |" + native.first_name + "    |" + native.last_name + "    |" + native.sex)
                print("\n==============================================================================================")


