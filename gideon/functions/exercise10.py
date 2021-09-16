def even_numbers():

    a = int(input("Enter first range: "))
    b = int(input("Enter last range: "))

    c = []
    for d in range(a, b):
        user = int(input("Input Number: "))
        c.append(user)
    even = []
    for x in c:
        if x % 2 == 0:
            even.append(x)
    print(even)