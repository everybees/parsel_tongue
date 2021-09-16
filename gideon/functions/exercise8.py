#Question 8
def unique_list():

    x = int(input("Enter first range: "))
    y = int(input("Enter last range: "))

    l = []
    for a in range(x,y):
        user = int(input("Input Number: "))
        l.append(user)

    number = []
    for n in l:
        if n not in number:
            number.append(n)
    return number