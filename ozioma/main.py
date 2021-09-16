from ozioma import chat_bot_2, calculator
from ozioma.function_module import exercises

if __name__ == "__main__":
    while True:
        value = int(input('Enter number between 1 and 11: '))
        if value == 1:
            print('Finding the maximum of three numbers')
            print(exercises.max_of_three_numbers())
        elif value == 2:
            print('Adding values in a list')
            print(exercises.add_values())
        elif value == 3:
            print('Summing of numbers in a list')
            print(exercises.sum_of_numbers_in_a_list())
        elif value == 4:
            print('Multiplying numbers in a list')
            print(exercises.multiply_numbers_in_a_list())
        elif value == 5:
            print('Reversing a string')
            print(exercises.reverse_a_string())
        elif value == 6:
            print('Finding the factorial of a number')
            print(exercises.factorial_of_a_number())
        elif value == 7:
            print('Checking if a number is within a range of inputted numbers')
            print(exercises.check_number_within_a_range())
        elif value == 8:
            print('Counting the number of upper and lower cases in a list')
            print(exercises.check_upper_and_lowercase_in_sentence())
        elif value == 9:
            print('Creating a list of unique values from a larger list')
            print(exercises.create_a_list_with_unique_elements_of_given_list())
        elif value == 10:
            print('Checking if a number is prime or not')
            print(exercises.find_prime_number())
        elif value == 11:
            print('Printing even numbers in a list')
            print(exercises.print_even_number_from_a_list())
        elif value == -1:
            print('Thank you for partaking in our game.')
            break


