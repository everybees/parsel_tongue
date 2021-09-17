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

cohort_eight_natives = []

import cohort_eight

if __name__ == "__main__":
    # create student
    student_1 = cohort_eight.create_student("Tife", "Olanipekun", "tifepekun@gmail.com","08066778899", "male")
    cohort_eight_natives.append(student_1)
    student_2 = cohort_eight.create_student("Yetunde", "Boluwatife", "yetundebolu@gmail.com","08066778890", "female")
    cohort_eight_natives.append(student_2)
    student_3 = cohort_eight.create_student("Demola", "Adeniyi", "demolaniyi@gmail.com","08066778891", "male")
    cohort_eight_natives.append(student_3)
    student_4 = cohort_eight.create_student("John", "Oladeji", "johnola@gmail.com","08066778892", "male")
    cohort_eight_natives.append(student_4)

    student_1["courses"].append("java")
    student_2["courses"].append("java")

    for element in cohort_eight_natives:
        if "java" not in element["courses"]:
            element["courses"].append("java")

print(cohort_eight_natives)
    # native = cohort_eight.Native("Tife", "Bolu")
    # print(native.first_name, native.last_name)