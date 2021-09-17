b = int(input("Enter a value for breadth:"))
l = 6 + b
h = 3 + l
def area_of_a_square(l, b):
    return l * b 

def volume(l, b, h):
    return l * b * h    

print("Area is:", area_of_a_square(l, b))
print("Volume is:", volume(l, b, h)) 