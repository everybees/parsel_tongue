minimum_hour = int(input("lower limit(hour) of sleep: "))
maximum_hour = int(input("upper limit(hour) of sleep: "))
hour_of_sleep = int(input("hours of sleep: "))
if(hour_of_sleep >= minimum_hour and hour_of_sleep <= maximum_hour):
    print("Normal")
elif(hour_of_sleep < minimum_hour):
    print("Deficiency")
else:
    print("Excess")
    