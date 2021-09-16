import question1
import question2
import question3
import question4
import question5
import question6
import question7

if __name__ == "__main__":
    while True:
        prompt = int(input("Select from options 1-10: "))
        if prompt == 1:
            question1.max_of_three_numbers()
        elif prompt == 2:
            question2.addition_of_list([1, 2, 3])
        elif prompt == 3:
            question3.multiplication_of_list([2, 3])
        elif prompt == 4:
            question4.reverse_of_string()
        elif prompt == 5:
            question5.factorial(5)
        elif prompt == 6:
            question6.test_range(5)
        elif prompt == 7:
            question7.string_test("The man is Crazy")
        else:
            print("Enter from 1-7 only")








