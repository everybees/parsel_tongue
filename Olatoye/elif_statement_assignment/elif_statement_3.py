def language_classifier(index):
	if index > 3:
		print("Polysynthetic")
	elif index < 2:
		print("Analytic")
	else:
		print("Synthetic")
		
print("Enter Index of Synthesis")
language_classifier(float(input()))

