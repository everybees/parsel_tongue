numbers_of_sleep_hours = 6
maximum_hours_of_sleep = 10

user_sleep_hours = int(input("how many hours do u sleep\n"))

if (user_sleep_hours > maximum_hours_of_sleep):
    print("excess")
if (user_sleep_hours < numbers_of_sleep_hours):
    print ("deficiency")
if  (user_sleep_hours >= numbers_of_sleep_hours and user_sleep_hours <= maximum_hours_of_sleep ):
    print("normal")