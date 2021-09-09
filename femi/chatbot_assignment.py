import random
data={
    "movie": ["F9", "Me before you", "fault in our stars", "Fatherhood", "Nobody"], 
    "book" : ["the subtle art of not giving a fuck", "an ugly truth", "think like a monk", "A promised land", "will"],
    "song": ["ojuelegba", "try me", "ye", "dear mama", "changes", "caught by a ghost", "unsteady"],
    "team": ["arsenal", "manchester united", "chelsea", "liverpool"],
    "tech": ["apis", "routers", "middlewares", "frameworks"],
}

print("Hi, I am Dami; ask me anything")

try:
    while True:
        question = input().split()
        for word in question:
            if word.strip("?") in data.keys():
                print(random.choice(data[word.strip("?")]))
                break
        else:
            print("I no sabi that one ooo")

except KeyboardInterrupt:
    print("\nexiting...")