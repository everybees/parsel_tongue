# the program checks if the year is a leap year
# when the year is inputted, the program checks if the input is divisible by 4 and not 100
# Or if it is divisible by 400
# Display "Leap year" or "Ordinary"
#

year_input = int(input("Enter year: "))


def leap_year_calculator():
    if year_input % 4 == 0 and year_input % 100 != 0 or year_input % 400 == 0:
        print("Leap year")
    else:
        print("Ordinary")


leap_year_calculator()
