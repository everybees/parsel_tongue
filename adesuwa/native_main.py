import native


if __name__ == '__main__':
    natives1 = []
    student1 = native.Natives("Blessing", "Sajon", "SCNO1", "F")
    natives1.append(student1)
    student2 = native.Natives("Shola", "Samuel", "SCNO2", "M")
    natives1.append(student2)

    natives2 = []
    student3 = native.Natives("Maltina", "Bassey", "SCNO3", "F")
    natives2.append(student3)
    student4 = native.Natives("Matthew", "Dwarf", "SCNO4", "M")
    natives2.append(student4)
   
    cohorts = []
    cohort1 = native.Cohorts("Cohort One Natives:", "First Alpha Set", natives1)
    cohorts.append(cohort1)
    cohort2 = native.Cohorts("Cohort Two Natives: ", "Second set to be admitted", natives2)
    cohorts.append(cohort2)
    cohort3 = native.Cohorts("Cohort Three Natives: ", "The great minds", natives1)
    cohorts.append(cohort3)
    cohort4 = native.Cohorts("Cohort Four Natives: ", "The searchers", natives2)
    cohorts.append(cohort4)

    building = native.Building("Building Name: Semicolon Village", cohorts)
    print(building.building_name)
    print("SCN No.  | First Name  | Last Name  | Sex  |  NativeID")
    print("-"*54)

    for coh in building.cohort:
        for native in coh.native:
            print(native.first_name, " |", native.last_name, " |", native.nativeID, " |", native.sex)