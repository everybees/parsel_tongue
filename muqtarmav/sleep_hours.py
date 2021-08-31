A = int(input("enter A Hours: "))
B = int(input("enter B Hours: "))
H = int(input("enter 'H' Ann sleeps Hours: "))

if H < A:
    print("deficiency")
if H > B:
    print("excess")
if H >= A and H <= B:
    print("normal")

