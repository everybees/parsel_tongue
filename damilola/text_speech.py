#numbers= ["zero","one","two","three","four","five","six","seven","eight","nine"]
#digit = input("Enter digit"+ " ")

#for number in digit:
#    print(numbers[int(number)])

a = [1,2,3,4,5]
b = "1,7,3,4,5"
c = 23
d = 2.3
e = str(2.3)

if len(b) > 4:
    for i in range(len(a)):
        if c < 20:
            print("a")
        else:
            for j in a:
                print(j,i)
                