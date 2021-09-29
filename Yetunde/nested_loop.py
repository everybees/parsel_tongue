# numbers = "54321"

# for number in numbers:
#     for i in number:
#         print(i)

a = [1, 2, 3, 4, 5]
b = "12345"
c = 23
d = 2.3

# for i in range(2, len(b)):
#     print(i)
#     while c > 21:
#         print(i, c)
#         c -= 1


if len(b) > 4:
    for i in range(len(a)):
        if c < 20:
            print("a")
        else:
            for j in a:
                print(j,i)
while c > 15:
    for i in b:
        print(i**i)
    c -=1        