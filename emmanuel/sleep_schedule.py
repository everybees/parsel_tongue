a_hours_of_sleep_recommended = int(input())

b_hours_of_sleep_required = int(input())

h_hours_of_sleep = int(input())

if a_hours_of_sleep_recommended >+ 6 and a_hours_of_sleep_recommended <= 10:
    print("Deficiency")
elif b_hours_of_sleep_required > 8 :
    print("Excess")
elif h_hours_of_sleep >=8 and h_hours_of_sleep <= 10:
    print("Normal")  
elif h_hours_of_sleep > 10:
     print("Exess")     
else:
    print("Deficiency")