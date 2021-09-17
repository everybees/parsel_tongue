value = float(input("Enter your value\n"))

# value_double = double(value)

if value < 2:
    print("Analytic")
elif  2 <= value <= 3:
    print("synthetic")
elif value > 3:
    print("Polysynthetic")