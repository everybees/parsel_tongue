
def enemy_classification(army):
    if army<1:
        print("no army")
    elif army>0 and army<10:
        print("few")
    elif army>9 and army<50:
        print("pack")
    elif army>49 and army<500:
        print("horde")
    elif army>499 and army<1000:
        print("swarm")
    else:
        print("legion")

army=int(input())
enemy_classification(army)    