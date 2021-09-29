
from foreverchild import exercise


if __name__ == "__main__":

    while True:
        print("User should enter any number from 1 to 10: ")
        user_number = int(input())
        if user_number > 10:
            print("wrong input")
            print("Exiting...")
            break
        if 1 == user_number:
            exercise.max_of_three_number()
        elif 2 == user_number:
            exercise.sum_of_numbers_in_a_list()
        elif 3 == user_number:
            exercise.product_of_numbers_in_a_list()
        elif 4 == user_number:
            exercise.reverse_a_string()
        elif 5 == user_number:
            exercise.factorial_of_a_number()
        elif 6 == user_number:
            exercise.number_in_a_range()
        elif 7 == user_number:
            exercise.number_of_upper_and_lower_case()
        elif 8 == user_number:
            exercise.unique_element_list()
        elif 9 == user_number:
            exercise.check_if_a_number_is_a_prime_number()

