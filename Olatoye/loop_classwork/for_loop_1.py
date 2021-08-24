def vowel():
	vowels = "aeiou"
	string = input("Enter your string: ").lower()
	number = 0
	
	for letter in string:
		if letter in vowels:
			number += 1
	print(number)
	
vowel()
