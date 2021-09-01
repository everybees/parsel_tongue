a = [1, 2, 3, 4, 5]
b = "17345"
c = 23
if len(b) > 4:
    for i in range(len(a)):
        if c < 20:
            print(a)
        else:
            for j in a:
                print(j, i)
    while c > 15:
        for i in b:
            print(int(i)**int(i))
        c -= 1
