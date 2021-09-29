from functions import cohort_records
if __name__ == "__main__":
    main_building = cohort_records.Building("Semicolon Village", "312 Herbert Macaulay, Sabo, Yaba")   
    native_1 = cohort_records.Native("1", "Sam", "Paul", "M")
    native_2 = cohort_records.Native("2", "Grace", "Favour", "F")
    cohort_1 = cohort_records.Cohort("Cohort One Natives")
    cohort_1.cohort_natives.append(native_1.__str__())
    cohort_1.cohort_natives.append(native_2.__str__())
    main_building.cohorts.append(cohort_1.__str__())

    native_2_1 = cohort_records.Native("1", "Victor", "Olamide", "M")
    native_2_2 = cohort_records.Native("2", "Tosin", "Akinnusi", "M")
    cohort_2 = cohort_records.Cohort("Cohort Two Natives")
    cohort_2.cohort_natives.append(native_2_1.__str__())
    cohort_2.cohort_natives.append(native_2_2.__str__())
    main_building.cohorts.append(cohort_2.__str__())

    native_3_1 = cohort_records.Native("1", "Precious", "Joy", "F")
    native_3_2 = cohort_records.Native("2", "Ahmad", "Ajala", "M")
    cohort_3 = cohort_records.Cohort("Cohort Three Natives")
    cohort_3.cohort_natives.append(native_2_1.__str__())
    cohort_3.cohort_natives.append(native_3_2.__str__())
    main_building.cohorts.append(cohort_3.__str__())

    native_4_1 = cohort_records.Native("1", "Muqtar", "Adetunji", "M")
    native_4_2 = cohort_records.Native("2", "Dami", "Omolori", "F")
    cohort_4 = cohort_records.Cohort("Cohort Four Natives")
    cohort_4.cohort_natives.append(native_4_1.__str__())
    cohort_4.cohort_natives.append(native_4_2.__str__())
    main_building.cohorts.append(cohort_4.__str__())

    print(main_building)
   
