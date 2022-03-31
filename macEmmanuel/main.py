import class_task

if __name__ == "__main__":
    add_natives = []
    native1 = class_task.native_method("SCN01", "Jack", "Janet", "Female")
    native2 = class_task.native_method("SCN02", "Jackie", "Jade", "Female")
    native3 = class_task.native_method("SCN03", "Jacky", "Jan", "Male")
    native4 = class_task.native_method("SCN04", "Jac", "Jane", "Male")
    print(class_task.get_natives())

#
# next_of_kin1 = first_example.create_next_of_kin("quin", "ajohne", "07062783014", "female", "wife")
# next_of_kin.append(next_of_kin1)
# first_example.register_native_to_cohort("segun", "john", "male", "08024355419", "sleepyjohn@gmail.com", next_of_kin)
# print(first_example.cohort_eight[0].next_of_kin[0].first_name)
