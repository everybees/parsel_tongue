numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

digits = input()

for digit in digits:
    #print (digit, ":", numbers[int(digit)])
    print (numbers[int(digit)], end=' ')

# to print on a straigth ine use end=" "