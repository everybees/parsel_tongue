# the program checks if the year is a leap year
# when the year is inputted, the program checks if the input is divisible by 4 and not 100
# Or if it is divisible by 400
# Display "Leap year" or "Ordinary"
#

def leap_year_calculator():
    year_input = int(input("Enter year: "))

    if year_input % 4 == 0 and year_input % 100 != 0 or year_input % 400 == 0:
        print("Leap year")
    else:
        print("Ordinary")


leap_year_calculator()


# write two numbers
# show the biggest number on the first line and smallest number on the second line

def number_size_checker():
    first_number = int(input())
    second_number = int(input())
    biggest_number = first_number
    if second_number > first_number:
        biggest_number = second_number
        print(biggest_number)
        print(first_number)
    else:
        print(first_number)
        print(second_number)


number_size_checker()