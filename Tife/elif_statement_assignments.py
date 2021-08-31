# Assignment 
A = int(input("enter a number: "))
B = int(input ("enter a number: "))
H = int(input("enter a number: "))

if  H < A :
    print("Deficiency")
elif H > B:
    print("Excess")
elif H > A and H < B:
    print("Normal")

language_number= int(input("Enter language number: "))
if language_number < 2 :
    print("Analytic")
elif language_number >= 2 and language_number <=3:
    print("Synthetic")
elif language_number > 3:
    print("Polysynthetic")     

number = int(input("Enter a number: ")) 
if number < 0:
    print("Negative")
if number == 0:
    print("Zero")
if number > 0:
    print("Positive")        