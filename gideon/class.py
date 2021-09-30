# def do_something(a=0, b="", c = []):
#     b = int(b)
#     d = a + b
#     c.append(d)
#     return c


# print(do_something(5.2,"5", ))

# length, breadth, breadth
# area = length * breadth
# volume = length * breadth * height

breadth = int(input("Enter a breadth: "))

def find_length(b):
    return 6 + b

def find_height(l):
    return 3 + l

volume = find_length(b=12) * breadth * find_height(l=30)
print(volume)

area = find_length(b=12) * breadth
print(area)

# def volume_area(l, b, h=1):
#     return l * b * h

# something = find_length(breadth) + find_height(find_length(breadth))
# print(something)

# something_one = 


# br = input(("Enter a number: "))

# def area(br, a, c):
#     return br * a * c
# something = area(br, 6, 3)
# print(something)

# number = int(input("Input number: "))

# def first_fun(first_number):
#     return first_number

# def second_fun(second_number):
#     return second_number

# final_result = first_fun(number) + second_fun(second_number=70)
# print(final_result)