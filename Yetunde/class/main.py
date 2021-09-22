from typing import no_type_check_decorator
import cohort_natives

if __name__ == "__main__":
    cohorts = []
    native1 = []
    native2 = []
    native3 = []
    native4 = []
    native_one = cohort_natives.Native("Abigeal", "Ola", "F", "SCN01")
    native1.append(native_one)
    native_one = cohort_natives.Native("Andrew", "Ola", "M", "SCN02")
    native1.append(native_one)
    cohort1 = cohort_natives.Cohort("cohort_one", "Phoenix", native1)
    cohorts.append(cohort1)
    
    
    native_two = cohort_natives.Native("Oluwadare", "Tomisin", "M", "SCN02")
    native2.append(native_two)
    native_three = cohort_natives.Native("Racheal", "Olamide", "F", "SCN03")
    native3.append(native_three)
    native_four = cohort_natives.Native("Racheal", "Olamide", "F", "SCN03")
    native4.append(native_four)
     
    
    
    cohort2 = cohort_natives.Cohort("cohort_two", "Sages", native2)
    cohorts.append(cohort2)
    cohort3 = cohort_natives.Cohort("cohort_three", "Plato", native3)
    cohorts.append(cohort3)
    cohort4 = cohort_natives.Cohort("cohort_four", "Gadans", native4)
    cohorts.append(cohort4)
    
    
    building = cohort_natives.Building("Semicolon village", cohorts)
    
    print("Building name: ", building.building_name)
    
    for cohort in building.cohorts:
        if cohort.cohort_name == "cohort_one":
            print ("Cohort: ",cohort.cohort_name)
            print("SCN  No.|   First name   |   Last name   |   sex")
            for native in cohort.natives:
                    print(native.id +   "   |"      + native.first_name +  "         |"  + native.last_name  +
                          "            |" + native.sex)
        if cohort.cohort_name == "cohort_two":
            print ("Cohort: ",cohort.cohort_name)
            print("SCN  No.|   First name   |   Last name   |   sex")
            for native in cohort.natives:
                    print(native.id +   "   |"      + native.first_name +  "         |"  + native.last_name  +
                          "            |" + native.sex)           
        if cohort.cohort_name == "cohort_three":
            print ("Cohort: ",cohort.cohort_name)
            print("SCN  No.|   First name   |   Last name   |   sex")
            for native in cohort.natives:
                    print(native.id +   "   |"      + native.first_name +  "         |"  + native.last_name  +
                          "            |" + native.sex)
        if cohort.cohort_name == "cohort_four":
            print ("Cohort: ",cohort.cohort_name)
            print("SCN  No.|   First name   |   Last name   |   sex")
            for native in cohort.natives:
                    print(native.id +   "   |"      + native.first_name +  "         |"  + native.last_name  +
                          "            |" + native.sex)
