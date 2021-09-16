#Question 7
def upper_lower_case():
    sentence = input("Enter Sentence: ")
    print("Lower case letters: ", sum(1 for a in sentence if a.islower()))
    
    print("Upper case letters: ", sum(1 for b in sentence if b.isupper()))