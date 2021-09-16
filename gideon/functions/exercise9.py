#Question 9
def check_prime():
    n = int(input("Enter digit: "))
    if (n == 1):
        return False
    elif (n == 2):
        return True
    for a in range(2, n//2):
        if n % a ==0:
            print("Not Prime")
    else:
        print("Prime")