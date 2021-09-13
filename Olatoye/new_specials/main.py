from Olatoye.functions.exercise import pangram
from Olatoye.new_specials import chatbot, calculator
from Olatoye.functions import exercise

if __name__ == "__main__":
    # userInput = int(input())
    # if userInput == 1:
    #     calculator.calculator()
    # elif userInput == 2:
    #     chatbot.chatbot()

    # exercise.max_of_three_numbers(4, 2, 3)
    # exercise.sum_of_numbers((1, 2, 2))
    # exercise.multiple_of_numbers((1, 2, 2))
    # exercise.reverse_string("olatoye")
    # exercise.factorial(4)
    # exercise.number_in_range(3, 1, 5)
    # exercise.upper_and_lower("OlaToye")
    # exercise.unique_list_item((1, 1, 3, 4, 5, 2, 1, 2))
    # exercise.prime_number(17)
    # exercise.even_number_from((1, 2, 3, 4, 5, 6))
    # exercise.perfect_number(6)
    # exercise.palindrome("madam")
    # exercise.pangram("The quick brown fox jumps over the lazy dog")
    # exercise.hyphen_separator("green-red-yellow-black-white")
    # exercise.squared_numbers()
    exercise.number_of_unique_local_variables(pangram("sentence"))
