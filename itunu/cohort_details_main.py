import cohort_details
if __name__ == "__main__":
    whole_building = cohort_records.Building("Semicolon Village", "312 Herbert Macaulay, Sabo, Yaba")   
    native_1 = cohort_details.Native("1", "Samuel", "Adeola", "M")
    native_2 = cohort_details.Native("2", "Shola", "Ola", "M")
    cohort_1 = cohort_details.Cohort("Cohort One Natives")
    cohort_1.cohort_natives.append(native_1.__str__())
    cohort_1.cohort_natives.append(native_2.__str__())
    main_building.cohorts.append(cohort_1.__str__())

    native_2_1 = cohort_details.Native("1", "Fatai", "Ade", "M")
    native_2_2 = cohort_details.Native("2", "Olu", "Akin", "M")
    cohort_2 = cohort_details.Cohort("Cohort Two Natives")
    cohort_2.cohort_natives.append(native_2_1.__str__())
    cohort_2.cohort_natives.append(native_2_2.__str__())
    whole_building.cohorts.append(cohort_2.__str__())

    native_3_1 = cohort_details.Native("1", "Goodnews", "James", "M")
    native_3_2 = cohort_details.Native("2", "Faith", "Joy", "F")
    cohort_3 = cohort_details.Cohort("Cohort Three Natives")
    cohort_3.cohort_natives.append(native_2_1.__str__())
    cohort_3.cohort_natives.append(native_3_2.__str__())
    whole_building.cohorts.append(cohort_3.__str__())

    native_4_1 = cohort_details.Native("1", "Muqtar", "Adetunji", "M")
    native_4_2 = cohort_details.Native("2", "Yetunde", "Olatunji", "F")
    cohort_4 = cohort_details.Cohort("Cohort Four Natives")
    cohort_4.cohort_natives.append(native_4_1.__str__())
    cohort_4.cohort_natives.append(native_4_2.__str__())
    whole_building.cohorts.append(cohort_4.__str__())

    print(whole_building)