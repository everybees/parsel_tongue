import random, time


database = {
    "male": ['I am male', 'I did love to meet with another male', 'I am a guy, I love men too'],
    "female": ['I did love to meet a male', 'I am a lady', 'I am a lesbian', 'I love men', 'Men piss ne off'],
    "hobbies": ['I love singing', 'i love dancing', 'i love swimming', ' i love fishing',
                'i love partying with friends',
                'i love evening meals with my family'],
    "life plans": ['I did want to tour the world', 'i did love to own my business', ' i did love to meet great minds',
                   'I want be a millionaire', 'I dont know', 'Headache'],
    "type of men": ['i like tall men', 'i like rich men', ' i like handsome men', ' i like them big',
                    'i like them rude',
                    'i like them saucy', 'I love dark men', 'I am attracted to fair men', 'I want a party man',
                    'I want a calm, cool and easy going guy i can control',
                    'I love rock men with tattoos and power bikes'],
    "type of women": ['i like bursty ladies', 'I like short ladies',
                      'i love sexy ladies with beautiful curves that i can die for',
                      'I love women with brain and beauty', 'I want a lady that can turn me up and down',
                      'I like them fair', 'I like them dark', 'I like them slim', 'I like them with spicy flesh',
                      'I love them churchy'],
    "country": ['Africa', 'Asia', 'USA', 'France', 'Paris', 'Chain', 'Indian', 'Britain', 'Italy', 'Romain', 'Canadan',
                'Spain']
}

print("Introduction, likes, interest etc....")

while True:
    time.sleep(1)
    sentence = input("Enter something:\n").split()

    if ['exit'] == sentence:
        print('Exiting...')
        break

    options = []

    for word in sentence:
        word = word.lower()
        if word in database.keys():
            options.append(random.choice(database[word]))

        if options:
            print(random.choice(options))
        else:
            print("Bring more spice Ideas.. Thanks")
