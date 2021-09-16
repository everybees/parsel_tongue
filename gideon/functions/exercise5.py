# Question 5
import math
def factorial():
    a = int(input("Enter digit: "))
    b = 1
    for c in range(2, a + 1):
        b *= c
    print(b)