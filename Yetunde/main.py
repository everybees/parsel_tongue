import chat_bot1
import calculator
from functions import exercise

print("""
      1. maximum_of_three_numbers
      2. sum_of_number_in_a_list
      3. multiply_numbers
      4. reverse_a_string
      5. calculate_factorial
      6. check_range
      7. Test_for_case
      8. check_unique_list
      9. PrimeNumber
      10. even_number
      """)
if __name__ == '__main__':
    userInput = int(input("Enter number: "))
    if userInput == 1:      
        print (exercise.max_of_three_numbers(a = int(input()), b = int(input()), c = int(input())))
    elif userInput == 2:
        print(exercise.sum_of_number_in_a_list([5,6,9,3,5,12]))
    elif userInput == 3:
        exercise.multiply_numbers()
    elif userInput == 4:
        print(exercise.reverse_a_string("gloria"))
    elif userInput == 5:
        print(exercise.calculate_factorial())
    elif userInput == 6:
        exercise.check_range()
    elif userInput == 7:
        print(exercise.test_for_case(s))
    # elif userInput == 8:
    elif userInput == 9:
        print(exercise.prime_number(13))
    elif userInput == 10:
       exercise.even_number([2,4,5,7,8,3,15,2,3,13,24,6,8,10])
        