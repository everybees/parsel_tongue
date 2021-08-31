# Ann inputs the excepted hours of sleep, the excess no of hours and no of sleep hours
# First number is always lesser than the second number
# If sleep hour is less than first number, display "Deficiency"
# If sleep hour is greater than second number, display "Excess"
# If sleep hour is greater than sleep hour and lesser than excess no of hours, display "Normal"
#
print('Enter the required no of sleep hours.')
a = int(input())
b = int(input())


if a < b:
    h = int(input())
    if h < a:
        print('Deficiency!')
    elif h > b:
        print('Excess!')
    elif a < h < b:
        print('Normal!')
else:
    print('Inputs are not valid')
