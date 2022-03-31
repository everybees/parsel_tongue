from typing import no_type_check_decorator
import cohort_natives

if __name__ == "__main__":
      Building = int(input("How many buildng do you want to create"))
      cohorts = int(input("How many cohorts do you want to create in the buildng"))
      Native = int(input("How many do you want in each building"))
      
      cohorts = []
      native1 = []
      native2 = []
      native3 = []
      native4 = []
      native_one = cohort_natives.Native("Abigeal", "Ola", "F", "SCN01")
      native1.append(native_one)
      native_one = cohort_natives.Native("Andrew", "Ola", "M", "SCN02")
      native1.append(native_one)
      native_one = cohort_natives.Native("Busola", "Sofowora", "F", "SCN03")
      native1.append(native_one)
      cohort1 = cohort_natives.Cohort("cohort_one", "Phoenix", native1)
      cohorts.append(cohort1)
  
      native_two = cohort_natives.Native("Oluwadare", "Tomisin", "M", "SCN01")
      native2.append(native_two)
      native_two = cohort_natives.Native("Oluwadamilola", "Owolabi", "F", "SCN02")
      native2.append(native_two)
      native_two = cohort_natives.Native("Chukwuemeka", "Amarachi", "M", "SCN03")
      native2.append(native_two)
      cohort2 = cohort_natives.Cohort("cohort_two", "Sages", native2)
      cohorts.append(cohort2)
    
      native_three = cohort_natives.Native("Racheal", "Olamide", "F", "SCN01")
      native3.append(native_three)
      native_three = cohort_natives.Native("Shuaib", "Mohammad", "M", "SCN02")
      native3.append(native_three)
      native_three = cohort_natives.Native("Adetoun", "Ola", "F", "SCN03")
      native3.append(native_three)
      cohort3 = cohort_natives.Cohort("cohort_three", "Plato", native3)
      cohorts.append(cohort3)
    
    
      native_four = cohort_natives.Native("Racheal", "Olamide", "F", "SCN03")
      native4.append(native_four) 
      native_four = cohort_natives.Native("Folakemi", "Olawatobi", "F", "SCN03")
      native4.append(native_four) 
      native_four = cohort_natives.Native("Udoh", "Gideon", "M", "SCN03")
      native4.append(native_four) 
      cohort4 = cohort_natives.Cohort("cohort_four", "Gadans", native4)
      cohorts.append(cohort4)
    
    
      building = cohort_natives.Building("Semicolon Village", cohorts)
    
      print("Building name: ", building.building_name)
    
      for cohort in building.cohorts:
          if cohort.cohort_name == "cohort_one":
              print ("Cohort: ",cohort.cohort_name)
              print("=" * 50)
              print("SCN  No.|   First name   |   Last name   |   sex")
              print("-" * 50)
              for native in cohort.natives:
                    print(native.id +   "   |"      + native.first_name +  "         |"  + native.last_name  +
                          "            |" + native.sex)
                    print("-" * 50)
                    
          if cohort.cohort_name == "cohort_two":
              print ("Cohort: ",cohort.cohort_name)
              print("=" * 50)
              print("SCN  No.|   First name   |   Last name   |   sex")
              print("-" * 50)
              for native in cohort.natives:
                    print(native.id +   "   |"      + native.first_name +  "         |"  + native.last_name  +
                          "            |" + native.sex)
                    print("-" * 50)
          if cohort.cohort_name == "cohort_three":
              print ("Cohort: ",cohort.cohort_name)
              print("=" * 50)
              print("SCN  No.|   First name   |   Last name   |   sex")
              print("-" * 50)
              for native in cohort.natives:
                    print(native.id +   "   |"      + native.first_name +  "         |"  + native.last_name  +
                          "            |" + native.sex)
                    print("-" * 50)
          if cohort.cohort_name == "cohort_four":
              print ("Cohort: ",cohort.cohort_name)
              print("=" * 50)
              print("SCN  No.|   First name   |   Last name   |   sex")
              print("-" * 50)
              for native in cohort.natives:
                    print(native.id +   "   |"      + native.first_name +  "         |"  + native.last_name  +
                          "            |" + native.sex)
                    print("-" * 50)
        
        