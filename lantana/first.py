a_hours = float(input())
b_hours = float(input())
h_hours = float(input())

if h_hours < a_hours:
    print("Deficiency")
elif h_hours > b_hours:
    print("Excess")
elif h_hours > a_hours and h_hours < b_hours:
    print("Normal")
