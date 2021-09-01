import random

print("Hello, please enter University of Choice")

universities = {"Harvard": ["GRE is Required for Nigerians", "TOEFL Is Optional for Nigerians",
                            "GRE Is Optional for First Class Students", "GRE is Recommended for ALL"],
                "Oxford": ["No Application Fees for UK Nationals", "You Cannot Apply into Oxford without GSSCE",
                           "No Tuition fee for citizens", "You will pay Application fees"],
                "MIT": ["App fee waiver for In-State Applicants", "Full tuition waiver for Intl. Student",
                        "1% chance of getting in", "App Deadline has Passed"],
                "UIC": ["No app waiver", "It is Cold in Chicago you might need your sweatshirt", "No jobs on campus for undergrads",
                        "GRE required for full funding", "No loud Music on campus"],
                "Stanford": ["No Chance of Getting admitted", "We located In the Bay area", "No application fee",
                             "We only accept Californians", "Stanford is the best university in the world", ]}
while True:
    question = input()
    for uni in universities:
        if uni in question:
            print(random.choice(universities[uni]))