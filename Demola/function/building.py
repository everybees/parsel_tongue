import datetime

import self as self


class Buiding:
    def __init__(self, name, description, cohorts) -> None:
        self.name = name
        self.description = description
        self.cohorts = cohorts
        self.date_created = datetime.datetime.now()

        def __str__(self) -> str:
            return self.name


class Cohort:
    def __init__(self, name, description, natives):
        self.name = name
        self.description = description
        self.natives = natives

    def __str__(self) -> str:
        return self.name


class Native:
    def __init__(self, scn, first_name, last_name, sex):
        self.scn = scn
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex


def _native_first_name(first_name):
    if len(first_name) > 25:
        raise ValueError("First name can not be above 25 characters")
    return first_name


def _native_last_name(last_name):
    if len(last_name) > 25:
        raise ValueError("Last name can not be above 25 characters ")
    return last_name

