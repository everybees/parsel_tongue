user_response = int (input("enter any number "))
divis = user_response % 2
if divis == 0 and user_response > 5 and user_response < 21 :
    print ("Weird")
if divis == 0 and user_response > 1 and user_response < 6:
    print ("Weird")
if divis == 0 and user_response > 20:
    print (" Not Weird")
else:
    print("Weird")