from functions import exercise

if __name__== "__main__":
    print("""
        1. Check for maximum number
        2. Sum of numbers in a list
        3. Multiple of numbers in a list
        4. Reverse strings
        5. Factorial of number
        6. Number in given range
        7. String counter
        8. List unique elements
""") 

user_input= int(input("Choose which function you wish to make use of:"))

if user_input == 1:
    print(exercise.max_of_three_numbers())
elif user_input == 2:
    exercise.sum_of_a_list()
elif user_input == 3:
    exercise.multiply_numbers_in_a_list()
elif user_input == 4:
    print(exercise.reverse_string())
elif user_input == 5:
    print(exercise.factorial())
elif user_input == 6:
    exercise.number_fall_in_a_given_range()
elif user_input == 7:
    exercise.string_counter()
else:
    print(exercise.list_unique_elements())    
