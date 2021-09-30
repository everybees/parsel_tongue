import correction
import Building, Cohort

building = {
    "name": "Semicolon Village",
    "description": "Growing Talent",
    "cohorts": [
        {
            "name": "cohort one",
            "description": "Thes are the alpha",
            "natives": [
                {
                    "scn": "",
                    "first_name": "",
                    "last_name": "",
                    "sex": ""
                }
            ]
        }
    ]
}

# sex = building['cohorts'][0]['natives'][0]['sex']
# print(sex)


def create_building(name, description, cohorts):
    building = Building(name, description, cohorts)
    return building


def create_cohort(name, description, natives):
    cohort = Cohort(name, description, natives)
    return cohort


def create_native(scn, first_name, last_name, sex):
    native = Native(scn, first_name, last_name, sex)
    return native


def print_native_data():
    print("Building Name: ", building['name'])
    print("Description ", building['description'])
    print("="*15)
    for cohort in building['cohorts']:
        print("Cohort Name: ", building['cohorts'][0]['name'])
        print("Cohort Description: ", building['cohorts'][0]['description'])
        print("SCN NO.0 \tFirst Name\tLast Name\tSex")
        print("-"*30)
        # for cohort in building['cohorts']:
        #     for native in cohort['natives']:
        for native in building['cohorts'][0]['natives']:
            print(native['scn'] + "\t\t" +
            native['first_name'] + "\t\t" +
            native['last_name'] + "\t\t" +
            native['sex']
                  )
            print('-'*30)


print_native_data()
