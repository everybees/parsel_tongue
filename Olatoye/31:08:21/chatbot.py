import datetime
import time, random

def chatbot():
	response = "yes"
	while response == "yes":

		question = input("What's that your question sef?\n").lower()
	
		love = ["Ja, ich liebe dich!", "Nein, ich liebe dich nicht", "Scheiße", "Love is wicked"]
		age = [num for num in range(1, 100)]
		eat = ["Yeah, baby!", "Nah 😢"]
		single = ["I'm single as feck", "It's like I'm in one relationship like that joor"]
		programs = ["python", "java", "golang", "c#"]
		country = ["Canada", "the UK", "Kenya", "Latvia"]
	
		if "time" in question:
			print(f"\nThe time is {datetime.datetime.now().time()}")
		elif "name" in question:
			print("\nAsk me something else biko")
		elif "love" in question:
			print(random.choice(love))
		elif "age" in question or "old" in question:
			print(random.choice(age))
		elif "eat" in question:
			print(random.choice(eat))
		elif "single" in question or "relationship" in question:
			print(random.choice(single))
		elif "play" in question or "fun" in question:
			print("It depends, ask no more")
		elif "code" in question or "program" in question:
			print("Yeah, I write only " + random.choice(programs) + " tho")
		elif "travel" in question or "country" in question:
			print("I've been to " + random.choice(country))
		elif "sleep" in question or "rest" in question or "shutdown" in question:
			print("I can't shutdown, I can only have a 10sec power nap daily")
		elif "ai" in question or "destroy" in question or "end" in question:
			print("I can only say AI won't be the end of humanity")
		else:
			print("\nOgbeni, are you normal?")
		
		time.sleep(1)
		print()
	
		response = input("Do you want to chat more? (yes or no)\n").lower()
		if response == 'no':
			print("Bye!")

chatbot()
