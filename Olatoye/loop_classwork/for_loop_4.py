def reverse_pattern():
	for i in range(5, 0, -1):
		for j in range(i, 0, -1):
			print(i, end=" ")
			i -= 1
		print()
				
reverse_pattern()

