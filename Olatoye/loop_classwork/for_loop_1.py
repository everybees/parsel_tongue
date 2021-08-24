def vowel():
	vowels = "aeiou"
	string = input("Enter your string: ").lower()
	number = 0
	
	for alphabet in vowels:
		if alphabet in string:
			number += 1
	print(number)
	
vowel()
