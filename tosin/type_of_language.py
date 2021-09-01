index = float(input("index of synthesis: "))
if(index < 2):
    print("Analytic")
elif(index >= 2 and index <=3):
    print("Synthetic")
else:
    print("Polysynthetic")