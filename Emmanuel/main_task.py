from functions import class_excercise

if __name__== "__main__":

    native = []
    cohort = []


    native_1 = class_excercise.Native("Jonnie", "JAY","M", "20", "SCN01")
    native.append(native_1)
    native_2 =class_excercise.Native("Yetunde", "Femi", "F", "24", "SCNO2")
    native.append(native_2)

    cohort_1 = class_excercise.Cohort("Cohort 1", "High fliers", native)
    cohort.append(cohort_1)

    building = class_excercise.Building("Semicolon", cohort)

    print(building.building_name)

    for cohort in building.cohorts:
        print(cohort.cohort_name +","+ cohort.cohort_description)
        print("SCN NO.    | First Name        |   Last Name      | Gender | Age ")
        print("====================================================================") 
        for native in cohort.natives:           
                print(native.cohort_id+"      |        " +native.first_name+"     |      "+ native.last_name+"        |        "+native.sex +"   |   "+ native.age)

