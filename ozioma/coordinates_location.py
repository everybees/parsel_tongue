# User sends input of two numbers in
# The quadrant is determined with first input as x and second input as y
# if first number is greater than 0 and between 0 and 10
#     and second value is between 0 and 10 and greater than 0;
#     then the coordinate is in the first quadrant. Display I
# If the first number is lesser than 0, between 0 and -10 and second number
#     is greater than 0, and is between 0 and 10, then it is second quadrant
#     Display II
# If the first input is lesser than 0 and between 0 and -10 and second number
#     is lesser than 0 and between 0 and -10; then it is the third quadrant.
#     Display III
# If tne first number is greater than 0 and between 0 and 10 and the second
#     number is lesser than 0 and between 0 and -0, then it is the fourth
#     quadrant. Display IV
# If any of the nos is zero, display "One of the coordinates is equal to zero"
#
# public class CoordinatesLocation {
#     public static void main(String[] args) {
#
#         Scanner scanner = new Scanner(System.in);
print("Enter two coordinates")
firstValue = int(input())
secondValue = int(input())
firstQuadrantIsTrue = firstValue > 0 and secondValue > 0
secondQuadrantIsTrue = firstValue < 0 < secondValue
thirdQuadrantIsTrue = firstValue < 0 and secondValue < 0
fourthQuadrantIsTrue = firstValue > 0 > secondValue
isOnTheCoordinate = firstValue == 0 or secondValue == 0

if firstQuadrantIsTrue: print("I")
if secondQuadrantIsTrue: print("II")
if thirdQuadrantIsTrue: print("IiI")
if fourthQuadrantIsTrue: print("IV")
if isOnTheCoordinate: print("One of the coordinates is equal to zero.")
