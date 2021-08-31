a = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
for i in a:
    if i % 2 != 0:
        print(i)

a = ["k","i","m"]
for b in a:
    print(b)

digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

my_number = input('Enter your number:')

for a in my_number:
    if a == "1":
        print(digits[0])
    elif a == "2":
        print(digits[1])
    elif a == "3":
        print(digits[2])
    elif a == "4":
        print(digits[3])

for i in range(5, 2):
    print(i, end=" ")



a = [1,2,3,4,5,6]
b = "17345"
c = 23

if len(b) > 4:
    for i in range(2,len(b)):
        if c < 20:
            print(a)
        else:
            for j in a:
                print(j,i)
    while c > 15:

        for i in b:
            print(int(i) ** int(i))
            c-=1

number = ""
for i in range(5):
    number = number + str(i + 1) + " "
    print(number)

number = 5
for i in range(0, number + 1 ):
    for j in range(number - 1, 0, -1):
        print(j, end=" ")
    print()














