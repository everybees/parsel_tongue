language = float(input())

if language < 2:
    print("Analytic")
elif language > 2 and language <=3:
    print("Synthetic")
else:
    print("Polysynthetic")