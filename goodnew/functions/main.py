import class_work

if __name__=="__main__":
    natives1=[]
    natives2 = []
    natives3=[]
    natives4=[]


    cohorts =[]
    native1= class_work.Native("John", "Frank","M", "SCN01")
    native2= class_work.Native("Johnny", "Tommy", "M", "SCN02")
    native3= class_work.Native("Janet", "jide", "M", "SCN03")
    native4= class_work.Native("Jimmy", "jolly","F", "SCN04")
    native5= class_work.Native("simon", "Timmy","M", "SCN05")
    native6= class_work.Native("Jamie", "Rice", "F", "SCN06")
    native7= class_work.Native("Kelly", "Doe","M", "SCN09")
    native8= class_work.Native("Minranda", "Doe","M", "SCN07")
    natives1.append(native1)
    natives1.append(native2)
    natives2.append(native3)
    natives2.append(native4)
    natives2.append(native5)
    natives3.append(native6)
    natives3.append(native7)
    natives4.append(native8)
   
    
    new_cohort = class_work.Cohort("cohort_one", "first cohort admitted into semicolon", natives1)
    cohorts.append(new_cohort)
    new_cohort = class_work.Cohort("cohort_two", "second cohort accepted into semicolon",natives2)
    cohorts.append(new_cohort)
    new_cohort = class_work.Cohort("cohort_three", "third cohort accepted into semicolon",natives3)
    cohorts.append(new_cohort)
    new_cohort = class_work.Cohort("cohort_four", "fourth cohort accepted into semicolon",natives4)
    cohorts.append(new_cohort)
    building = class_work.Building("Semicolon Village", cohorts)
    print (building.name)
    
    for cohort in building.cohorts:
        if cohort.name == "cohort_one":
            print (cohort.name+":")
            print("SCN  No.|   First name   |   Last name   |   sex")
            for native in cohort.natives:
                print(native.native_id +   "        |"     + native.first_name + "          |"  + native.last_name  + "         |" + native.sex)
        
            print("="*50)

        elif cohort.name=="cohort_two":
            print (cohort.name+":")
            print("SCN  No.|   First name   |   Last name   |   sex")
            for native in cohort.natives:
                print(native.native_id +   "        |"     + native.first_name + "          |"  + native.last_name  + "         |" + native.sex)

            print("="*50)

        elif cohort.name == "cohort_three":
            print (cohort.name+":")
            print("SCN  No.|   First name   |   Last name   |   sex")
            for native in cohort.natives:
                print(native.native_id +   "        |"     + native.first_name + "          |"  + native.last_name  + "         |" + native.sex)
            print("="*50)
        else:
            print(cohort.name+":")
            print("SCN  No.|   First name   |   Last name   |   sex")
            for native in cohort.natives:
                print(native.native_id +   "        |"     + native.first_name + "          |"  + native.last_name  + "         |" + native.sex)
            print("="*50)
