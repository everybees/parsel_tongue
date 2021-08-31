# the user inputs a number which can be translated to text
# To do this, we loop through the input digits
# Each digit is named according to previously declared number equated text
# for number in text:
# for digit in number:
# print(text)

text = ["zero, one, two, three, four, five, six, seven, eight, nine"]
numbers = ["0123456789"]
digits = input("Enter number: ")
for number in numbers:
    for digit in digits:
        if digit in number:
            print(text[number])