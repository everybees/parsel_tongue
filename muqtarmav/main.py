from Functions import exercise

if __name__ == "__main__":
    print("Enter a number from 1 - 10 to make use of a specific function")
while True:
    print("Enter number from 1-10 to continue or any other number to exit")
    number = int(input("Enter a number: "))
    if number == 1:
        print("Maximum number is: ", exercise.max_of_three_numbers())
    elif number == 2:
        print("Total is: ", exercise.sum_in_a_list())
    elif number == 3:
        print("Total is: ", exercise.multiply_numbers_in_list())
    elif number == 4:
        print("New word is: ", exercise.string_reverse())
    elif number == 5:
        print("Answer is: ", exercise.factorial_number())
    elif number == 6:
        print(exercise.range_no())
    elif number == 7:
        exercise.count_lower_and_uppercase()
    elif number == 8:
        print("New list is: ", exercise.unique_list())
    elif number == 9:
        print(exercise.test_prime())
    elif number == 10:
        print("New list of even number is : ", exercise.even_number_in_list())
    else:
        print("Exiting")
        break
# if __name__ == "__main__":
#     print("enter any number from 1 to 10: ")
#     while True:
#         user_number = int(input("enter number from 1-10"))
#         if user_number == 1:
#             print(exercise.max_of_three_number())
#         elif 2 == user_number:
#             exercise.sum_in_a-list()
#         elif 3 == user_number:
#             exercise.multiply_numbers_in_a_list()
#         elif 4 == user_number:
#             exercise.string_reversre()
#         elif 5 == user_number:
#             exercise.factorial_number()
#         elif 6 == user_number:
#             exercise.range_no()
#         elif 7 == user_number:
#             exercise.count_lower_and_uppercase
#         elif 8 == user_number:
#             exercise.unique_list()
#         elif 9 == user_number:
#             exercise.test_prime()
#         elif 10 == user_number:
#             exercise.is_even_number()
#         else:
#             print("Existing")
#             break
#
#
#
