import datetime
import random

print("Whats your plans for the future?")

skills = ["Problem Solving", "Leadership", "Self-Motivation", "Communication", "Teamwork"]
education = ["Bachelors", "Masters", "PhD"]
career = ["Software Engineering", "Digital Marketing", "Animal farming", "Cateering and Information", "Marketing", "Geology", "Surveying"]
business = ["Yes", "No"]
year = ["year duration", "In century", "In decades", "Millennium"]
country = ["USA", "Germany", "Canadan", "Britians", "France"]
job = ["Yes", "No", "Still not sure", "I love my business"]

while True:
    question = input()
    
    if "Year" in question:
        print(random.choice(year))
    elif "course" in question or "subject" in question or "best course" in question:
        print(random.choice(career))
    elif "handworks" in question or "skills" in question or "works" in question:
        print(random.choice(skills))
    elif "place" in question or "location" in question or "dream views" in question:
        print(random.choice(country))
    elif "University Degree" in question or "Level of education" in question or "Discipline" in question:
        print("I did love to read", random.choice(education))
    elif "own a shop" in question or "Shop" in question or "business" in question:
        print(random.choice(business))
    elif "why" in question or "thinking" in question:
        print("Im on my own world cloud plans and life")
    elif "job" in question:
        print("In what filed?", random.choice(job))
        break
    else:
        print("Look for a plan B")
        