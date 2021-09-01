A = 8
B = 10
H = int(input())


if (H < A):
    print('Defficiency')
elif (H > B):
    print('Excess')
elif H in range(A and B):
    print('Normal')

