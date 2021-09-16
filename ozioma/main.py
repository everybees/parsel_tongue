from ozioma import chat_bot_2, calculator
from ozioma.function_module import exercises

if __name__ == "__main__":
    while True:
        value = int(input('Enter number between 1 and 11: '))
        if value == 1:
            print(exercises.max_of_three_numbers())
        elif value == 2:
            print(exercises.add_values())
        elif value == 3:
            print(exercises.sum_of_numbers_in_a_list())
        elif value == 4:
            print(exercises.multiply_numbers_in_a_list())
        elif value == 5:
            print(exercises.reverse_a_string())
        elif value == 6:
            print(exercises.factorial_of_a_number())
        elif value == 7:
            print(exercises.check_number_within_a_range())
        elif value == 8:
            print(exercises.check_upper_and_lowercase_in_sentence())
        elif value == 9:
            print(exercises.create_a_list_with_unique_elements_of_given_list())
        elif value == 10:
            print(exercises.find_prime_number())
        elif value == 11:
            print(exercises.print_even_number_from_a_list())
        else:
            print('Thank you for partaking in our game.')


