number_in_word = ["zero", "one", "two", "three", "four", "five", "six", "seven", 'eight', "nine"]

digits = input()
for digit in  digits:
    print(digit, ":", number_in_word[int(digit)])