from precious.oop.object_oriented_programming import object_oriented_programming

if __name__ == "__main__":
    main_building = object_oriented_programming.Building("Semicolon Village", "312 Herbert Macaulay, Sabo, Yaba\n\n")
    native_1 = object_oriented_programming.Native(sc_id=input("Enter your Semi colon id no\t"), first_name=
    input("Enter First Name\t"), last_name=input("Enter Last name\t"), sex=input("Enter Sex\t"))
    native_2 = object_oriented_programming.Native(sc_id=input("Enter your Semi colon id no\t"), first_name=
    input("Enter First Name\t"), last_name=input("Enter Last name\t"), sex=input("Enter Sex\t"))
    cohort_1 = object_oriented_programming.Cohort(cohort_name=input("Enter name of cohort"))
    cohort_1.cohort_natives.append(native_1.__str__())
    cohort_1.cohort_natives.append(native_2.__str__())
    main_building.cohorts.append(cohort_1.__str__())

    native_2_1 = object_oriented_programming.Native(sc_id=input("Enter your Semi colon id no\t"), first_name=
    input("Enter First Name\t"), last_name=input("Enter Last name\t"), sex=input("Enter Sex\t"))
    native_2_2 = object_oriented_programming.Native(sc_id=input("Enter your Semi colon id no\t"), first_name=
    input("Enter First Name\t"), last_name=input("Enter Last name\t"), sex=input("Enter Sex\t"))
    cohort_2 = object_oriented_programming.Cohort(cohort_name=input("Enter name of cohort"))
    cohort_2.cohort_natives.append(native_2_1.__str__())
    cohort_2.cohort_natives.append(native_2_2.__str__())
    main_building.cohorts.append(cohort_2.__str__())

    native_3_1 = object_oriented_programming.Native(sc_id=input("Enter your Semi colon id no\t"), first_name=
    input("Enter First Name\t"), last_name=input("Enter Last name\t"), sex=input("Enter Sex\t"))
    native_3_2 = object_oriented_programming.Native(sc_id=input("Enter your Semi colon id no\t"), first_name=
    input("Enter First Name\t"), last_name=input("Enter Last name\t"), sex=input("Enter Sex\t"))
    cohort_3 = object_oriented_programming.Cohort(cohort_name=input("Enter name of cohort"))
    cohort_3.cohort_natives.append(native_2_1.__str__())
    cohort_3.cohort_natives.append(native_3_2.__str__())
    main_building.cohorts.append(cohort_3.__str__())

    native_4_1 = object_oriented_programming.Native(sc_id=input("Enter your Semi colon id no\t"), first_name=
    input("Enter First Name\t"), last_name=input("Enter Last name\t"), sex=input("Enter Sex\t"))
    native_4_2 = object_oriented_programming.Native(sc_id=input("Enter your Semi colon id no\t"), first_name=
    input("Enter First Name\t"), last_name=input("Enter Last name\t"), sex=input("Enter Sex\t"))
    cohort_4 = object_oriented_programming.Cohort(cohort_name=input("Enter name of cohort"))
    cohort_4.cohort_natives.append(native_4_1.__str__())
    cohort_4.cohort_natives.append(native_4_2.__str__())
    main_building.cohorts.append(cohort_4.__str__())

    print(main_building)
