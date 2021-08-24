
# assignment1
a_hours = int(input("enter first number:"))
b_hours = int(input("enter second number:"))
h_hours = int(input("enter third number:"))

if h_hours < a_hours :
    print("Deficiency")
elif h_hours > b_hours:
    print("Excess")
elif h_hours > a_hours or h_hours < b_hours:
    print("Normal")


# assignment2
x_coordinates = int(input("enter your x-coordinates:"))
y_coordinates = int(input("enter your y-coordinates:"))

if x_coordinates == 0 and y_coordinates == 0:
    print("it's the origin")

elif x_coordinates == 0 and y_coordinates != 0:
    print("one of the coordinate is equal to zero")

elif x_coordinates != 0 and y_coordinates == 0:
    print("one of the coordinate is equal to zero")
    println()

# assignment3
number = float(input("enter your number:"))

if number <= 2 :
    print("Analytic Language")
elif number > 2 and number < 3:
    print("Synthetic Language")
elif number >= 3:
    print("Polysynthetic Language")



# assignment 4
integer_number =int(input("send in your number ogagit"))

if integer_number < 0:
    print("negative")
if integer_number > 0:
    print("positve")
if integer_number == 0:
    print("zero")
