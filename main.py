import native
if __name__ == "__main__":
    main_building = native.Building("Semicolon Village", "312 Herbert Macaulay, Sabo, Yaba")   
    native_1 = native.Native("1", "Teslim", "Abdulkareem", "M")
    native_2 = native.Native("2", "Adeola", "Toyin", "F")
    cohort_1 = native.Cohort("Cohort One Natives")
    cohort_1.cohort_natives.append(native_1.__str__())
    cohort_1.cohort_natives.append(native_2.__str__())
    main_building.cohorts.append(cohort_1.__str__())

    native_2_1 = native.Native("1", "Demola", "demo", "M")
    native_2_2 = native.Native("2", "John", "Ogidi", "M")
    cohort_2 = native.Cohort("Cohort Two Natives")
    cohort_2.cohort_natives.append(native_2_1.__str__())
    cohort_2.cohort_natives.append(native_2_2.__str__())
    main_building.cohorts.append(cohort_2.__str__())

    native_3_1 = native.Native("1", "Opor", "Toe", "F")
    native_3_2 = native.Native("2", "Arinfesesi", "Femi", "M")
    cohort_3 = native.Cohort("Cohort Three Natives")
    cohort_3.cohort_natives.append(native_2_1.__str__())
    cohort_3.cohort_natives.append(native_3_2.__str__())
    main_building.cohorts.append(cohort_3.__str__())

    native_4_1 = native.Native("1", "Ahmad", "Ajala", "M")
    native_4_2 = native.Native("2", "Teniola", "Adeola", "F")
    cohort_4 = native.Cohort("Cohort Four Natives")
    cohort_4.cohort_natives.append(native_4_1.__str__())
    cohort_4.cohort_natives.append(native_4_2.__str__())
    main_building.cohorts.append(cohort_4.__str__())

    print(main_building)

   