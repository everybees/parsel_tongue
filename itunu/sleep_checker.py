A = int (input())
B = int (input())
H = int (input())

# A is always less then B
if A<B:
    if H<A:
        print("Deficiency")
    elif H>B:
        print("Excess")
    elif H>=A and H<=B:
        print("Normal")

    
    
