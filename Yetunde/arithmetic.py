time_str = input("Enter a time in seconds")
time_int = int(time_str)
hours = int(time_int / 60 /60)
minutes = int(time_int / 60)
seconds = int(time_int % 60)
print(hours,"hours,",minutes,"minutes", "and", seconds, "seconds")