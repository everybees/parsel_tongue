# import chat_bot
# if __name__ == "__main__":
#     chat_bot.do_something()

# import chat_bot, calculator
# if __name__== "__main__":
#     userInput = int(input("""
#     Enter: 1 for Calculator
#            2 for Chatbot
#     """))
#     if userInput == 1:
#         calculator.calculate_something()
#     else:
#         chat_bot.do_something()

import math
from functions import exercise

# if __name__== "__main__":
#     print(exercise.max_of_three_numbers())

# if __name__== "__main__":
#    print(exercise.sum_of_numbers_in_a_list())  

# if __name__== "__main__":
#    exercise.multiply_numbers_in_a_list()    

# if __name__== "__main__":
#    (exercise.reverse_string())

# if __name__== "__main__":
#    exercise.calculate_factorial_of_a_number()

# if __name__ == "__main__":
#     exercise.find_number_in_range()

# if __name__ == "__main__":
#     exercise.calculate_case_of_letter("i am a BOY")

# if __name__ == "__main__":
#     exercise.sum_of_numbers_in_a_list([2,3,4])

if __name__== "__main__":
    while True:
        prompt=int (input("Enter from numbers 1 to 10: "))
        if prompt==1:
            exercise.max_of_three_numbers()
        elif prompt==2:
            exercise.sum_of_numbers_in_a_list()
        elif prompt==3:
            exercise.multiply_numbers_in_a_list()
        elif prompt==4:
            exercise.reverse_string()
        elif prompt==5:
            exercise.calculate_factorial_of_a_number()
        elif prompt==6:
            exercise.find_number_in_range()
        elif prompt==7:
            exercise.calculate_case_of_letter()
        elif prompt==8:
            exercise.unique_list()
        elif prompt==9:
            print(exercise.check_ifprime())
        elif prompt==10:
            (exercise.is_even_list())
        else:
            print("invalid number")        


                                            








