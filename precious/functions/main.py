from precious import dictionary_two
from precious import calculator
from functions import exercise

print("\nWelcome to Precious' calculator service ")

# user_input = input("Enter 1 to perform first function and 2 to the second function and enter 3 to perform both "
#                  "function: ")
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
    user_inputs = exercise.maximum_of_three_numbers()
elif user_inputs == 2:
    user_inputs = exercise.sum_number([1, 2, 3, 4, 5])
elif user_inputs == 3:
    user_inputs = exercise.multiple([1, 2, 3, 4, 5])
elif user_inputs == 4:
    user_inputs = exercise.reverse_a_string("Precious")
elif user_inputs == 5:
    user_inputs = exercise.factorial(6)
elif user_inputs == 6:
    user_inputs = exercise.number_fall(4, 1, 10)
elif user_inputs == 7:
    user_inputs = exercise.string_uppercase_lowercase()
elif user_inputs == 8:
    user_inputs = exercise.unique_element([1, 2, 4, 4, 2, 6, 8])
elif user_inputs == 9:
    user_inputs = exercise.prime_number(7)
elif user_inputs == 10:
    user_inputs = exercise.even_number([1, 2, 3, 4, 5, 6, 7, 8])
elif user_inputs == 11:
    user_inputs = exercise.perfect_number(28)
elif user_inputs == 12:
    user_inputs = exercise.string_palindrome("madam")
elif user_inputs == 14:
    user_inputs = exercise.pangram("The quick brown fox jumps over the lazy dog")
elif user_inputs == 15:
    user_inputs = exercise.hyphen_separated_sequence("zulu-foxtrot-delta-tango-echo-bravo")
elif user_inputs == 16:
    user_inputs = exercise.value_square_numbers()
else:
    print("invalid number")
