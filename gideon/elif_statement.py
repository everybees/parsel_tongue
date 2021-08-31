# army = int(input())

# if army < 1:
#     print("no army")
# elif army >= 1 and army <= 9:
#     print("few")
# elif army >= 9 and army <= 49:
#     print("pack")
# elif army > 49 and army <= 499:
#     print("horde")
# elif army > 499 and army <= 999:
#     print("swarm")
# else:
#     print("legion")


num = int(input())
if num < 0:
    print("negative")
elif num > 0:
    print("positive")
elif num == 0:
    print("zero")