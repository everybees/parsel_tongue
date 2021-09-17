import exercise1

if __name__ == "__main__":
    while True:
        user_number = int(input("Enter function number from 1 to 10: "))
        if user_number > 10 or user_number <= 0:
            print("UNKNOWN COMMAND!!")
            print("Exiting main...")
            break
        if 1 == user_number:
            print(exercise1.max_of_three_numbers())
        elif 2 == user_number:
            exercise1.sum_of_numbers_in_a_list()
        elif 3 == user_number:
            exercise1.product_of_numbers_in_a_list()
        elif 4 == user_number:
            exercise1.reverse_print()
        elif 5 == user_number:
            exercise1.factorial()
        elif 6 == user_number:
            exercise1.num_in_range()
        elif 7 == user_number:
            exercise1.upper_lower_case()
        elif 8 == user_number:
            print(exercise1.unique_list())
        elif 9 == user_number:
            exercise1.check_prime()
        elif 10 == user_number:
            exercise1.even_numbers()