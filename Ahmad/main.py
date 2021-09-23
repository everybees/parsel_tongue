import Cohort_Class
if __name__ == "__main__":
    main_building = Cohort_Class.Building("Semicolon Village", "312 Herbert Macaulay, Sabo, Yaba")
    native_1 = Cohort_Class.Native("01", "Demola", "Big D", "M")
    native_2 = Cohort_Class.Native("02", "Favour", "Light", "F")
    cohort_1 = Cohort_Class.Cohort("Cohort One Natives")
    cohort_1.cohort_natives.append(native_1.__str__())
    cohort_1.cohort_natives.append(native_2.__str__())
    main_building.cohorts.append(cohort_1.__str__())

    native_2_1 = Cohort_Class.Native("01", "Tosin", "Beauty", "M")
    native_2_2 = Cohort_Class.Native("02", "Muqtar", "Crypto", "M")
    cohort_2 = Cohort_Class.Cohort("Cohort Two Natives")
    cohort_2.cohort_natives.append(native_2_1.__str__())
    cohort_2.cohort_natives.append(native_2_2.__str__())
    main_building.cohorts.append(cohort_2.__str__())

    native_3_1 = Cohort_Class.Native("01", "Teslim", "Teni or Nobody", "F")
    native_3_2 = Cohort_Class.Native("02", "Ahmad", "Ajala", "M")
    cohort_3 = Cohort_Class.Cohort("Cohort Three Natives")
    cohort_3.cohort_natives.append(native_2_1.__str__())
    cohort_3.cohort_natives.append(native_3_2.__str__())
    main_building.cohorts.append(cohort_3.__str__())

    native_4_1 = Cohort_Class.Native("01", "Muqtar", "Adetunji", "M")
    native_4_2 = Cohort_Class.Native("02", "Dami", "Oladimdim", "F")
    cohort_4 = Cohort_Class.Cohort("Cohort Four Natives")
    cohort_4.cohort_natives.append(native_4_1.__str__())
    cohort_4.cohort_natives.append(native_4_2.__str__())
    main_building.cohorts.append(cohort_4.__str__())

    print(main_building)
