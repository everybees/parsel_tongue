index_of_synthesis= float(input("Enter index of synthesis of desired language:\n"))

if index_of_synthesis < 2:
    print("Analytic")
elif index_of_synthesis>=2 and index_of_synthesis<=3:
    print("Synthetic")
elif index_of_synthesis>3:
    print("Polysynthetic")
    
    