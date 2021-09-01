string_number = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
number = input("Enter number: \n ")
#string = "vowel"
for digit in number:
    print(string_number[int(digit)], end=" ")
