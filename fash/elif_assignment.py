
# # assignment1
# a_hours = int(input("enter first number:"))
# b_hours = int(input("enter second number:"))
# h_hours = int(input("enter third number:"))
#
# if h_hours < a_hours :
#     print("Deficiency")
# elif h_hours > b_hours:
#     print("Excess")
# elif h_hours > a_hours or h_hours < b_hours:
#     print("Normal")
#
#
# # assignment2
# x_coordinates = int(input("enter your x-coordinates:"))
# y_coordinates = int(input("enter your y-coordinates:"))
#
# if x_coordinates == 0 and y_coordinates == 0:
#     print("it's the origin")
#
# elif x_coordinates == 0 and y_coordinates != 0:
#     print("one of the coordinate is equal to zero")
#
# elif x_coordinates != 0 and y_coordinates == 0:
#     print("one of the coordinate is equal to zero")
#     println()
#
# # assignment3
# number = float(input("enter your number:"))
#
# if number <= 2 :
#     print("Analytic Language")
# elif number > 2 and number < 3:
#     print("Synthetic Language")
# elif number >= 3:
#     print("Polysynthetic Language")
#
#
#
# # assignment 4
# integer_number =int(input("send in your number ogagit"))
#
# if integer_number < 0:
#     print("negative")
# if integer_number > 0:
#     print("positve")
# if integer_number == 0:
#     print("zero")


# student_heights = input("Enter your list please").split()
# for n in range (0,len(student_heights)):
#     student_heights[n] = int (student_heights[n])
#     print (len(student_heights))
# # print (sum(student_heights))





# import random
#
# names_Of_String = input("what are the names :")
# names = names_Of_String.split(",")
# length_of_names = len(names)
# random_Names = random.randint(0,length_of_names-1)
# names_Of_Buyer = names[random_Names]
# print(names_Of_Buyer +" is buying lunch today")


# total = 0
# for number in range(0,101,2):
#     total+= number
# print(total)


# for number in range(1,100):
#     if number % 3 == 0 and number % 5 == 0:
#         print("fizzBuzz")
#     elif number % 3 == 0:
#         print("fizz")
#     elif number % 5 == 0:
#         print("buzz")
#     else:
#         print(number)

def move_round():
    turn_left()
    move()
    turn_right()

    for number in range(1,21):
        move_round()