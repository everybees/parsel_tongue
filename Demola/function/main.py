import exercise

if __name__ == "__main__":
    while True:
        print("Number 1 for Max and Min")
        print("Number 2 for Addition")
        print("Number 3 for Multiplier")
        print("Number 4 for Text Reversing")
        print("Number 5 for Factorial")
        print("Number 6 for Number Boundary")
        print("Number 7 for Case Counter")
        print("Number 8 for Prime Numbers")
        print("Number 9 for Even Number Detector")
        print("Number 10 for Prime Number Tester")
        prompt = int(input("Choose a number: "))
        if prompt == 1:
             exercise.max_of_three_numbers()
        elif prompt == 2:
            exercise.lets_add_numbers()
        elif prompt == 3:
            exercise.multiplier()
        elif prompt == 4:
            exercise.textreverse()
        elif prompt == 5:
            exercise.factorial()
        elif prompt == 6:
            exercise.number_bound()   
        elif prompt == 7:
            exercise.case_counter()
        elif prompt == 8:
            exercise.prime_number()
        elif prompt == 9:
            exercise.even_number_detector()
        elif prompt == 10:
            exercise.prime_tester(4)           
        else:
            print("Exiting................................")
            break                                   
