import datetime
import time, random

def chatbot():
	response = "yes"
	while response == "yes":

		question = input("What's that your question sef?\n").lower()
	
		dictionary = {
		"time" : ["The time is " + str(datetime.datetime.now().time()) ,"Go buy wristwatch"],
		"name" : ["Siri", "Sam", "Alexa", "Ask me something else biko"],
		"love" : ["Ja, ich liebe dich!", "Nein, ich liebe dich nicht", "Scheiße", "Love is wicked"],
		"eat" : ["Yeah, baby!", "Nah 😢"],
		"single" : ["I'm single as feck", "It's like I'm in one relationship like that joor"],
		"programs" : ["I write python sometimes", "I'm learning java", "I can't kill myself on golang", "C# is unnecessarily hard"],
		"country":  ["I've been to Canada", "Maybe the UK", "Lovely Kenya", "Extremely beautiful Latvia"],
		"age" : ["I am ",  str(num for num in range(1, 100)), " old"],
		"play" : ["It depends tho", "Biko leave me alone joor", "Make I daze you?!"],
		"sleep" : ["I rarely sleep mehn", "I can't shutdown, I can only have a 10sec power nap daily"]
		}
		
		for key in dictionary.keys():
			if key == question:		
				print(random.choice(dictionary[key]))
			else:
				print("\nOgbeni, are you normal?")
				break
		
		time.sleep(1)
		print()
	
		response = input("Do you want to chat more? (yes or no)\n").lower()
		if response == 'no':
			print("Bye!")

chatbot()
