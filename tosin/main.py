from functions import exercise
if __name__ == "__main__":
    print("Enter a number from 1 - 10 to make use of a specific function")
    number = int(input("Enter a number: "))
if number == 1:
    print("This is a function that determines the maximum number of 3 different digits")
    print("Maximum number is: ",exercise.max_of_three_numbers())
elif number == 2:
    print("This is a function that perform addition of 5 numbers in a list")
    print("Total is: ", exercise.sum_of_numbers_in_a_list())
elif number == 3:
    print("This is a function that perform multiplication of 5 numbers in a list")
    print("Total is: ", exercise.multiply_numbers_in_list())
elif number == 4:
    print("This is a function that reverse a word")
    print("New word is: ", exercise.reverse_string())
elif number == 5:
    print("This is a function that calculate the factorial of a number")
    print("Answer is: ", exercise.calculateFactorial())
elif number == 6:
    print("This is a function that determines whether a number is in range lower limit and upper limit")
    print(exercise.find_range())
elif number == 7:
    print("This is a function that determines the number of uppercase and lowercase in a sentence")
    exercise.count_lower_and_uppercase()
elif number == 8:
    print("This is a function that generate unique list from pre-existing list")
    print("New list is: ", exercise.unique_list())
elif number == 9:
    print("This is a function that determines whether a number is a prime number or not")
    print(exercise.prime_number())
elif number == 10:
    print("This is a function that determines even numbers in a list")
    print("New list of even number is : ", exercise.even_number_in_list())
else:
    print("Invalid number selection.")
