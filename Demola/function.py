from Demola.building.building import Building, Cohort

from parsel_tongue.Demola.function.building import Native

building = {
    "name": "Semicolon",
    "description": "Tech Hub",

    "cohorts":[
        {
            "name": "",
            "description": "",
            "natives"[
                {
                    "scn": "",
                    "first_name": "",
                    "last_name": "",
                    "sex": ""
                }
            ]
        }
    ],
}
def create_building(name, description, cohorts):
    building = Building(name, description, cohorts)
    return building
def create_cohort(name, description, natives):
    cohort = Cohort(name, description, natives)
    return building
def  create_natives(scn, first_name, last_name, sex):
    native = Native(scn, first_name, last_name, sex)
    return native
def print_natives_date():
    print("Building Name: ",building['name'])
    print("Description: ", building['description'])
    print("=======================================")
    print("Cohort Name: ", building['cohorts'][0]['name'])
    print("Cohort Description: ", building['cohorts: '][0]['description'])
    print("SCN No. |\tFirst Name |\last Name |\tSex")
    print("-----------------------------------------")
    for cohort in building['cohorts']:
        for native in cohorts['natives']:
        print(native['scn'] + "\t|\t" +
        native['first_name'] + "\t|\t" +
        native['last_name'] + "\t|\t" +
        native['sex'])
    print("----------------------------------------")

    print_natives_date()
        # print(building['cohorts'][0]['natives'][0]['scn'] + "\t|"
        # building['cohorts'][0]['natives'][0]['first_name']
        # building['cohorts'][0]['natives'][0]['last_name']
        # building['cohorts'][0]['natives'][0]['sex'])