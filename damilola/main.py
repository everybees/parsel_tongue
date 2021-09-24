 import dami_cohort
if __name__ =="__main__":
   main_building = dami_cohort.Building("Semicolon Village", "312 Herbert Macaulay, Sabo, Yaba")
   native_1 =dami_cohort.Native("01", "Dimeji", "Tosh", "M")
   native_2 = dami_cohort.Native("02", "KK", "Neo", "F")
   cohort_1 = dami_cohort.Cohort("Cohort One Natives")
   cohort_1.dami_cohort.append(native_1.__str__())
   cohort_1.cohort_natives.append(native_2.__str__())
   main_building.cohorts.append(cohort_1.__str__())

   native_2_1 = dami_cohort.Native("01", "Solomon", "Akpan", "M")
   native_2_2 = dami_cohort.Native("02", "John", "ajasco", "M")
   cohort_2 = dami_cohort.Cohort("Cohort Two Natives")
   cohort_2.cohort_natives.append(native_2_1.__str__())
   cohort_2.cohort_natives.append(native_2_2.__str__())
   main_building.cohorts.append(cohort_2.__str__())

   native_3_1 = dami_cohort.Native("01", "Dami", "Tope or Nobody", "F")
   native_3_2 = dami_cohort.Native("02", "Gidi", "Udoh", "M")
   cohort_3 = dami_cohort.Cohort("Cohort Three Natives")
   cohort_3.cohort_natives.append(native_2_1.__str__())
   cohort_3.cohort_natives.append(native_3_2.__str__())
   main_building.cohorts.append(cohort_3.__str__())

   native_4_1 = dami_cohort.Native("01", "Mero", "tunji", "M")
   native_4_2 = dami_cohort.Native("02", "Dami", "Oladimdim", "F")
   cohort_4 = dami_cohort.Cohort("Cohort Four Natives")
   cohort_4.cohort_natives.append(native_4_1.__str__())
   cohort_4.cohort_natives.append(native_4_2.__str__())
   main_building.cohorts.append(cohort_4.__str__())

   print(main_building)
  
