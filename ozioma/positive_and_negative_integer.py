# take a number as input
# if the number is less than 0, print "Negative!"
# if the number is greater than 0, print "Positive!"
# if the number is equal to 0, print "Zero!"
print('Enter a value: ')
integer_value = int(input())

if integer_value < 0:
    print('Negative!')
elif integer_value > 0:
    print('Positive!')
elif integer_value == 0:
    print('Zero!')