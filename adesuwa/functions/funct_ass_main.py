import funct_assign
import math

if __name__ == '__main__':

    #exercise.max_of_three_numbers()
    #exercise.sum_of_list_numbers()
    #exercise.multiply_all_list_numbers()
    #exercise.factorial_of_a_number(6)
    #exercise.number_in_range(2500)
    # exercise.numbers_of_lower_and_uppercase("gygYGGk vghv vgvjgvvjvjhg VJGVJ")

    user_inputs = int(input(
        """
        Enter 
        1 to get the maximum number of three
        2 to get the sum of a list
        3 to get the multiple number of a list
        4 to get the reverse of a string
        5 to get the factorial number
        6 to get the number fall
        7 to get the upper case and lower case number
        8 to get the unique element
        9 to get the prime number
        10 to get even number
        11 to get the perfect number
        12 to get the string palindrome 
        14 to get the pangram
        15 to get the hyphen_separated_sequence
        16 to get value square numbers
        """
    ))
    if user_inputs == 1:
        user_inputs = funct_assign.max_of_three_numbers()
    elif user_inputs == 2:
        user_inputs = funct_assign.sum_of_list_numbers([1, 2, 3, 4, 5])
    elif user_inputs == 3:
        user_inputs = funct_assign.multiply_all_list_numbers([1, 2, 3, 4, 5])
    elif user_inputs == 4:
        user_inputs = funct_assign.reverse_a_string()
    elif user_inputs == 5:
        user_inputs = funct_assign.factorial_of_a_number(6)
    elif user_inputs == 6:
        user_inputs = funct_assign.number_in_range(2500)
    elif user_inputs == 7:
        user_inputs = funct_assign.numbers_of_lower_and_uppercase("Hello bkb NKB uhln JKHLKBN")
    elif user_inputs == 8:
        user_inputs = funct_assign.unique_element([1, 2, 4, 4, 2, 6, 8])
    elif user_inputs == 9:
        user_inputs = funct_assign.prime_number(7)
    elif user_inputs == 10:
        user_inputs = funct_assign.even_number([1, 2, 3, 4, 5, 6, 7, 8])
    elif user_inputs == 11:
        user_inputs = funct_assign.perfect_number(28)
    elif user_inputs == 12:
        user_inputs = funct_assign.string_palindrome("madam")
    elif user_inputs == 14:
        user_inputs = funct_assign.pangram("The quick brown fox jumps over the lazy dog")
    elif user_inputs == 15:
        user_inputs = funct_assign.hyphen_separated_sequence("zulu-foxtrot-delta-tango-echo-bravo")
    else:
        print("invalid number")

