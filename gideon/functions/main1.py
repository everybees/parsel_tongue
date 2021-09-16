import exercise1, exercise2, exercise3, exercise4, exercise5
import exercise6, exercise7, exercise8, exercise9, exercise10

if __name__ == "__main__":
    while True:
        user_number = int(input("Enter function number: "))
        if user_number > 10 or user_number <= 0:
            print("UNKNOWN COMMAND!!")
            print("Exiting main...")
            break
        if 1 == user_number:
            print(exercise1.max_of_three_numbers())
        elif 2 == user_number:
            exercise2.sum_of_numbers_in_a_list()
        elif 3 == user_number:
            exercise3.product_of_numbers_in_a_list()
        elif 4 == user_number:
            exercise4.reverse_print()
        elif 5 == user_number:
            exercise5.factorial()
        elif 6 == user_number:
            exercise6.num_in_range()
        elif 7 == user_number:
            exercise7.upper_lower_case()
        elif 8 == user_number:
            print(exercise8.unique_list())
        elif 9 == user_number:
            exercise9.check_prime()
        elif 10 == user_number:
            exercise10.even_numbers()