breadth = int(input("enter the breadth: "))

def find_length(b):
        return 6 + b

def find_height(l):
    return 3 + l

def volume_area(l, b, h=1):
    return l * b * h
    
something = find_length(breadth) + find_height(find_length(breadth))
print(something)