# import chat_bot_1

# if __name__ == "__main__":
#     chat_bot_1.do_something()

# from gideon import chat_bot_1
# import chat_bot_1, calculator

# if __name__ == "__main__":
#     while True:
#         user_number = int(input("Enter a number: "))
#         if user_number > 10:
#             print("UNKNOWN COMMAND!!")
#             print("Exiting main...")
#             break
#         if 1 == user_number:
#             chat_bot_1.do_something()
#         elif 2 == user_number:
#             calculator.calculate()


# from functions import exercise
# if __name__ == "__main__":
#     print(exercise.max_of_three_numbers(a=220, b=300, c=90))

# from functions import exercise
# if __name__ == "__main__":
#     exercise.sum_of_numbers_in_a_list([2,6,4,4,3,1,2])

# from functions import exercise
# if __name__ == "__main__":
#     exercise.product_of_numbers_in_a_list()


# from functions import exercise
# if __name__ == "__main__":
#     exercise.reverse_print()

# from functions import exercise
# if __name__ == "__main__":
#     exercise.factorial(a=5)

# from functions import exercise
# if __name__ == "__main__":
#     exercise.num_in_range(a=5, x=2, y=10)

# from functions import exercise
# if __name__ == "__main__":
#     exercise.upper_lower_case()

# from functions import exercise
# if __name__ == "__main__":
#     exercise.unique_list()

# cohort_eight_natives = []

# import cohort_eight

# if __name__ == "__main__":
#     # create student
#     student_1 = cohort_eight.create_student("Tife", "Olanipekun", "tifepekun@gmail.com","08066778899", "male")
#     cohort_eight_natives.append(student_1)
#     student_2 = cohort_eight.create_student("Yetunde", "Boluwatife", "yetundebolu@gmail.com","08066778890", "female")
#     cohort_eight_natives.append(student_2)
#     student_3 = cohort_eight.create_student("Demola", "Adeniyi", "demolaniyi@gmail.com","08066778891", "male")
#     cohort_eight_natives.append(student_3)
#     student_4 = cohort_eight.create_student("John", "Oladeji", "johnola@gmail.com","08066778892", "male")
#     cohort_eight_natives.append(student_4)

#     student_1["courses"].append("java")
#     student_2["courses"].append("java")

#     for element in cohort_eight_natives:
#         if "java" not in element["courses"]:
#             element["courses"].append("java")

# print(cohort_eight_natives)
    # native = cohort_eight.Native("Tife", "Bolu")
    # print(native.first_name, native.last_name)
# import second_example

# if __name__ == "__main__":
#     next_of_kin=[]
#     next_of_kin1 = second_example.create_next_of_kin("quin","ajohne","07062783014","female","wife")
#     next_of_kin.append(next_of_kin1)
#     second_example.register_native_to_cohort("segun", "john","male","08024355419","sleepyjohn@gmail.com",next_of_kin)
#     print(second_example.cohort_eight[0].next_of_kin[0].first_name)
import class_task

if __name__ == "__main__":
    native1 = []
    student1 = class_task.Natives("Yetunde", "Olasehinde", "female", "SCN No1")
    native1.append(student1)
    student2 = class_task.Natives("John", "Oladeji", "male", "SCN No2")
    native1.append(student2)

    native2 = []
    student3 = class_task.Natives("Emmanuel", "Olorunishola", "male", "SCN No3")
    native2.append(student3)
    student4 = class_task.Natives("Ozioma", "Okoroafor", "female", "SCN No4")
    native2.append(student4)

    native3 = []
    student5 = class_task.Natives("Tife", "Olanipekun", "male", "SCN No5")
    native3.append(student5)
    student6 = class_task.Natives("Adesuwa", "Odomela", "female", "SCN No6")
    native3.append(student6)

    native4 = []
    student7 = class_task.Natives("Kimberly", "Mojoyin", "female", "SCN No7")
    native4.append(student7)
    student8 = class_task.Natives("Olatoye", "Daramola", "male", "SCN No8")
    native4.append(student8)



    cohorts = []
    cohort_one = class_task.Cohort("Phoenix", "The Good People", native1)
    cohorts.append(cohort_one)
    cohort_two = class_task.Cohort("Sages", "I dont know", native2)
    cohorts.append(cohort_two)
    cohort_three = class_task.Cohort("Hoodlums", "Them just dey", native3)
    cohorts.append(cohort_three)
    cohort_four = class_task.Cohort("Acme", "Question Sir, primarily..", native4)
    cohorts.append(cohort_four)

    
    building = class_task.Building("Building Name: Semicolon Africa", cohorts)
    print("------------------------------------------------------------------------------")
    print(building.building_name)
    print("------------------------------------------------------------------------------")


    print("SCN No.     |    FIRST NAME         |   LAST NAME         |   SEX")
    print("------------------------------------------------------------------------------")

    
    for cohort in building.cohorts:
        for native in cohort.native:
            print(native.id + "     |        " +native.first_name+ "      |       " +native.last_name + "     |       " + native.sex)
            print("------------------------------------------------------------------------------")