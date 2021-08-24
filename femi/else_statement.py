
year = int(input())

if year%4==0 and year%100!=0 or year%400==0:
    print("Leap")
else:
    print("Ordinary")



def maximum():
    first_input=int(input())
    second_input=int(input())

    if first_input<second_input:
        print(second_input)
        print(first_input)
    else:
        print(first_input)
        print(second_input)

maximum()
    
