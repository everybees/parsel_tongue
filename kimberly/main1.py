import builtins
import class_task
if __name__ == "__main__":
    native1=[]
    native_1=class_task.Native("001","emma","jos","male")
    native1.append(native_1)
    native_2=class_task.Native("002","giddy","udoh","male")
    native1.append(native_2)
    native_3=class_task.Native("003","kim","oke","female")
    native1.append(native_3)
    native_4=class_task.Native("004","tife","bolu","male")
    native1.append(native_4)

    native2=[]
    native_1=class_task.Native("005","segun","mac","male")
    native2.append(native_1)
    native_2=class_task.Native("006","yetunde","ade","female")
    native2.append(native_2)
    native_3=class_task.Native("007","isreal","fashina","male")
    native2.append(native_3)
    native_4=class_task.Native("008","dami","omolori","female")
    native2.append(native_4)

    native3=[]
    native_1=class_task.Native("009","ozi","firebrand","female")
    native3.append(native_1)
    native_2=class_task.Native("010","demola","ade","male")
    native3.append(native_2)
    native_3=class_task.Native("011","tosin","aina","male")
    native3.append(native_3)
    native_4=class_task.Native("012","tesleem","abu","male")
    native3.append(native_4)

    native4=[]
    native_1=class_task.Native("013","solomon","tope","male")
    native4.append(native_1)
    native_2=class_task.Native("014","ahmad","ola","male")
    native4.append(native_2)
    native_3=class_task.Native("015","lantana","mohammed","female")
    native4.append(native_3)
    native_4=class_task.Native("016","adesuwa","omo","female")
    native4.append(native_4)

    cohort=[]
    cohort_1=class_task.Cohort("cohort_one","jan,2020",native1)
    cohort.append(cohort_1)
    cohort_2=class_task.Cohort("cohort_two","june,2020",native2)
    cohort.append(cohort_2)
    cohort_3=class_task.Cohort("cohort_three","jan,2021",native3)
    cohort.append(cohort_3)
    cohort_4=class_task.Cohort("cohort_four","june,2021",native4)
    cohort.append(cohort_4)


    building=class_task.Building("Semicolon Village",cohort)
     
    print("================================================")
    print(building.building_name)
    print("=================================================")

    print("SCN No. | First Name | Last Name | Sex")
    print("===================================================")
    for cohort in building.cohorts:
        for native in cohort.natives:
            print(native.scn_no     +"    |   "         + native.first_name     +"  |   "       +    native.last_name       +"  |   "       +   native.sex)

