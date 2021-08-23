sleep_A = int(input())
sleep_B = int(input())
sleep_H = int(input())

if sleep_A <= sleep_B:
    if sleep_H < sleep_A:
        print("Deficiency")
    elif sleep_H > sleep_B:
        print("Execes")
    elif sleep_H >= sleep_A and sleep_H <= sleep_B:
        print("Normal")