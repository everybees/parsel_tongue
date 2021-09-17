import Native
import Building
import Cohort

if __name__ == "__main__": 
    cohorts=[]
    natives=[]
    building = Building.Building("Semicolon Village", 1)
    cohort1 = Cohort.Cohort(1, "cohort_one", "first cohort admitted into semicolon")
    cohorts.append(cohort1)
    cohort2 = Cohort.Cohort(8, "phoenix", "the last cohort admitted")
    cohorts.append(cohort2)

    native1 = Native.Native("SCN01", "John", "Doe", "Male")
    natives.append(native1)
    native2 = Native.Native("SCN02", " Harry", " Doe", " Male")
    natives.append(native2)
print(" ")
print("Building Name: ", building.building_name)

print("Cohort ", cohort1.cohort_name)
print("SCN No." + " | "+ "First Name "+"|"+ " Last NAme"+ " |"+" Sex")
print("-------------------------------------")

for native in natives:
    print(native.native_id + "|"+ native.first_name+" | "+ native.last_Name+ " | "+ native.Sex)


print(" ")

