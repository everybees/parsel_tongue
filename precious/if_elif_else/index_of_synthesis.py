number = float(input("Enter number: \n"))

if number < 2:
    print("Analytic")
if 2 <= number <= 3:
    print("Synthetic")
elif number > 3:
    print("Polysynthetic")
