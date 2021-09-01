i=1
while(i<=5): 
    j=1
    while(j<=5):
        if j<i:
            print("*", end=' ')
        j+=1
    print()
    i+=1

k=5
while(k>0):
    j=k
    while(j>0):
        print("*", end=' ')
        j-=1
    print()
    k-=1