import class_task

if __name__=="__main__":
    natives1=[]
    natives2 = []
    cohorts =[]
    native1= class_task.Native("John", "Doe","M", "SCN01")
    natives1.append(native1)
    native2= class_task.Native("Johnny", "Doe", "M", "SCN02")
    natives1.append(native2)
    native3= class_task.Native("Jane", "Doe", "F", "SCN03")
    native4= class_task.Native("Jimmy", "Doe","M", "SCN04")
    native5= class_task.Native("Jane", "Doe","F", "SCN05")
    natives2.append(native3)
    natives2.append(native4)
    natives2.append(native5)
   
    
    new_cohort = class_task.Cohort("cohort_one", "first cohort admitted into semicolon", natives1)
    cohorts.append(new_cohort)
    new_cohort = class_task.Cohort("cohort_two", "second cohort accepted into semicolon",natives2)
    cohorts.append(new_cohort)
    building = class_task.Building("Semicolon Village", cohorts)
    print (building.name)
    
    print("SCN  No.|   First name   |   Last name   |   sex")

    for cohort in building.cohorts:
        for native in cohort.natives:
            print(native.native_id +   "        |"     + native.first_name + "          |"  + native.last_name  + "         |" + native.sex)
    
