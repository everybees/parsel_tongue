def army_classifier():
	army = int(input())
	
	if army >= 1000:
		print("Legion")
	elif 500 <= army <= 999:
		print("Swarm")
	elif 50 <= army <= 499:
		print("Horde")
	elif 10 <= army <= 49:
		print("Pack")
	elif 1 <= army <= 9:
		print("Few")
	else:
		print("No army")
		
army_classifier()

def 
