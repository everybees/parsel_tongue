number = float(input("The value of the index of synthesis is: "))

if number < 2:
  print("Analytic")
elif number >= 2 and number <=3:
    print("Synthetic")
elif number > 3:
    print("Polysynthetic")
