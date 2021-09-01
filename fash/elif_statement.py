army_number = int(input("enter you number: "))

if army_number < 1:
    print("no army")
elif army_number > 1 and army_number <= 9:
    print("few army")
elif army_number > 10 and army_number <=49:
    print("Pack of army")
elif army_number > 50 and army_number <= 499:
    print("swarm of army")
elif army_number >500 and army_number <= 999:
    print("legion of army")
else:
    print("Thosand of army")


a_hours = int(input("enter first number":))
b_hours = int(input("enter second number":))
h_hours = int(input("enter third number":))

if h_hours < a_hours :
    print("Deficiency")
elif h_hours > b_hours:
    print("Excess")
elif h_hours > a_hours || h_hours < b_hours:
    print("Normal")



