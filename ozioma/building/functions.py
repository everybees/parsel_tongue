from ozioma.building import class_task


def create_building(name, cohorts, address):
    building = class_task.Building(name, cohorts)
    return building


def create_cohort(name, natives, description):
    cohort = class_task.Cohorts(name,natives,description)
    return cohort


def create_native(first_name, last_name, native_id, gender):
    native = class_task.Native(first_name, last_name,native_id,gender)
    return native

