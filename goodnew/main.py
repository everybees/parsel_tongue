from functions import exercise

if __name__ == "__main__":
    
    print("""
        Kindly choose any of the options to select the operation to perform
        1. max_of_three_numbers
        2. sum_of_numbers_in_a_list
        3. product_of_numbers_in_a_list
        4. reverse-string
        5. factorial_of_number
        6. check_if_a_number-falls_in_the_range
        7. check_the_number_of_upper_case_and_lower_case_letters
        8. list_of_unique_number
        9. write_the_number_number_of_even_number_in_a_list
        10.prime_number
        """)
    
    user_input = int(input("Kindly select your desired function\n"))

    if user_input == 1:
        exercise.max_of_three_numbers()
    
    if user_input == 2:
        exercise.sum_of_numbers_in_a_list()
    
    if user_input == 3:
        exercise.product_of_numbers_in_a_list()
    
    if user_input == 4:
        exercise.reverse_a_string()
    
    if user_input == 5:
        exercise.factorial_of_a_number()
    
    if user_input == 6:
        exercise.check_whether_a_number_falls_in_a_given_range()
    
    if user_input == 7:
        exercise.calculate_number_of_uppercase_and_lowercase_letters()
        
    if user_input == 8:
        exercise.list_with_unique_element_of_the_first_list([1,2,3,2,1,2,1,1,5,6,1])
    
    if user_input == 9:
        exercise.prime_numbers()
        
    if user_input == 10:
        exercise.even_number([8, 9, 80, 23, 12])
