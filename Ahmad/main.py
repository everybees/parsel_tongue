from functions import exercise
if __name__ == "__main__":
    number = int(input("Enter number between 1-10 to select function: "))
if number == 1:
    print("This is a function that determines the maximum number of three different functions.")
    print("The maximum number is: ", exercise.max_of_three_numbers(321, 908, 543))
elif number == 2:
    print("This is a function that gives the sum of numbers in a a list")
    print("The sum of the numbers in the list are: ", exercise.sum_of_numbers_in_a_list(4, 5, 33, 1123, 6, 7, 9))
elif number == 3:
    print("This is a function that performs the multiplication of numbers in a list")
    print("total is: ", exercise.multiply_numbers_in_a_list(3, 5, 8, 9, 12, 3, 6, 7, 9))
elif number == 4:
    print("This is a function that prints the reverse of a word")
    print("word in reverse is: ", exercise.reverse())
elif number == 5:
    print("This is a function that calculates the factorial of a method")
       print("Factorial is: ", exercise.factorial(9))
elif number == 6:
    print("This is a function that checks if a number is within the 100 range")
    print("Number supplied ", exercise.range_checker(23))
elif number == 7:
    print("This is a function that counts the  number of upper and lower case letters in a given text")
    print("From the text given: ", exercise.case_calculator("NigerIa is Our country. wE sHOUlD fIx It"))
elif number == 8:
    print("This is a function that prints the unique elements in a given list")
    print("Unique elements in the given list are: ", exercise.unique_elements(2, 5, 6, 7, 8, 4, 2, 1, 1, 3, 9, 0))
elif number == 9:
    print("This is a function that determines whether a number is a prime number or not")
    print("Number supplied ", exercise.prime_number())
elif number == 10:
    print("This is a function that prints the even numbers present in a list")
    print("even numbers present in the list are: ", exercise.even_number_in_list(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
else:
    print("Invalid number selection. Please enter a valid number.")





