a = [1, 2, 3, 4, 5]
b = "17345"
c = 23

if len(b) > 4:
    for numb in range(len(a)):
        if c < 20:
            print("a")
        else:
            for numbs in a:
                print(numbs, numb)
    while c > 15:
        for numb in b:
            print(int(numb) ** int(numb))
            c -= 1
