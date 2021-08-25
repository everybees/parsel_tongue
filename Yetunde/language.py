index_of_synthesis= float(input("Enter index of synthesis for a language: "))

if index_of_synthesis < 2:
    print("Analytic")
elif 2 <= index_of_synthesis <= 3:
    print("Synthetic")
elif index_of_synthesis > 3:
    print("Polysynthetic")
    