army=int(input())

if army < 1:
    print("No Army")

elif 1 >= army and army <= 10:
    print("Few")

elif 10 <= army and army <=49:
    print("Pack")

elif 50 >= army and army <= 499:
        print("Horde")

elif 500 <= army and army >=  999:
    print("Swarm")

else:
    print("Legion")