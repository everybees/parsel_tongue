number_words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]

number_values = input("Enter your number\n")

for number in number_values:
    print(number_words[int(number)])
