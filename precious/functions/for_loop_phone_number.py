number = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
phone_number = input("Enter number \n")

for digit in phone_number:
    print(number[int(digit)])
