# length, breadth, height
# area = length * breadth
# volume = length * breadth * height

# breadth = int(input("Enter the breadth: "))
# length = 6 + breadth
# height = 3 + length

# def volume_area(length, breadth, height=1):
#     return length* breadth* height

# print("area = ", volume_area(length, breadth)) 
# print("volume = ", volume_area(length, breadth, height)) 

breadth = int(input("Enter the breadth: "))

def find_length(b):
    return 6 + b

def find_height(l):
    return 3 + l

def volume_area(l, b, h=1):
    return l * b * h

result = find_length(breadth) + find_height(find_length(breadth))
print(result)