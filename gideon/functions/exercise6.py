# Question 6
def num_in_range():

    x = int(input("Enter first range: "))
    y = int(input("Enter second range: "))
    a = int(input("Enter number: "))

    if a in range(x, y):
        print("Yes! Number in range")
    else:
        print("No! Number not in range")