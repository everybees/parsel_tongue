import datetime

import random

# who is the first President of Nigeria?
# Who is the current President of Nigeria?
# Is Nigeria developed
# What are the tourist attractions in NIgeria?
# Give me examples of Nigerian Foods.



print("My name  Ade, how may I be of help to you today?")

President = ["The current President of Nigeria is Buhari", "The first President of Nigeria is Nnamdi Azikiwe"]
Independent  = ["Nigeria gained independence in 1960"]
Food = [" Example of Nigrian food includes, Eba, Fufu and Tuwo"]
Development = ["Yes, Nigeria is a develop  nation", "Nigeri is not a developed Nations", "Lets aske Ifa"]
Tourist = ["Tourist attraction in Nigeria includes Olumo rock, Gurara falls, Ogbunike cave"]

while True:
    question = input()
    if "current" in question:
        print("The current president of Nigeria is Muhammadu Buhari")
    elif "name" in question:
        print("My name is Ade, how may I be of help to you today?")
    elif "first" in question:
        print("The first President of Nigeria is Nnamdi Azikiwe")
    elif "Independent" in question:
        print("Nigeria gained independence in 1960")
    elif "food" in question:
        print("Example of Nigerian food includes, Eba, Fufu and Tuwo")
    elif "tourist" in question:
        print("Tourist attraction in Nigeria includes Olumo rock, Gurara falls, Ogbunike cave")
    else:
        print("I don't understand")


