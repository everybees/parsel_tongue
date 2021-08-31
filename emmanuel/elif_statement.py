category = int(input())

if category < 1:
    print("no army")
elif 1 <= category & category <= 9:
    print("few")
elif 10 <= category & category <= 49:
    print("pack")
elif 50 <= category & category <= 490:
    print("horde")
elif 500 <= category & category <= 999:
    print("swarm")
else:
    print("legion")
