user_input = int(input("Please select an option between 1 and 5\n"))

if user_input == 1:
    print("function that adds two numbers together and produces the sum to a user")
    def add_two_numbers():
        a=int(input("Enter first number:\n"))
        b=int(input("Enter second number:\n"))
        total = a + b
        print("sum of the two numbers is", total)
    add_two_numbers()
elif user_input == 2:
    print("function takes two or more numbers, sums them together and tells the user the sum of the numbers")
    def add_numbers(numbers):
        total = 0
        for number in numbers:
            total = total+ int(number)
        print(total)
    add_numbers(input("enter numbers you wish to have added together").replace(',', ''))
elif user_input == 3:
    print("function takes a word and reverses the word")
    def reverse_string(word):
       print(word[::-1])
    reverse_string(input("enter word you wish to have reversed"))
elif user_input == 4:
    print("function takes a group of numbers and returns a sorted list of the numbers")
    def sort_list(numbers):
        _list=[]
        for number in numbers:
            _list.append(int(number))
        _list.sort()
        print(_list)
    sort_list(input("enter group of numbers you wish to have sorted").split(','))
