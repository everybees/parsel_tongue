x = float (input("Enter first coordinate point:\n"))
y = float (input("Enter second coordinate point:\n"))

if (x!=0 and y!=0):
    if x>0 and y>0:
        print("I")
    elif (x<0 and y>0):
        print("II")
    elif (x<0 and y<0):
        print("III")
    else:
        print("IV")
else:
    print("Its the origin!")
        

