language = float(input("The value of the index: "))

if language < 2:
    print("Analytic")
elif language > 3:
    print("Polysynthetic")
else:
    print("Synthetic")
