import re

from util import *

day = 4


def task1():
    data = get_input_for_day(day)
    # data = get_input_for_file("test")
    valid = 0
    d = dict(
        [("byr", False), ("iyr", False), ("eyr", False), ("hgt", False), ("hcl", False), ("ecl", False),
         ("pid", False)])

    data.append("")
    for line in data:
        if line == "":
            if all(val for val in d.values()):
                valid += 1
            d = dict([("byr", False), ("iyr", False), ("eyr", False), ("hgt", False), ("hcl", False), ("ecl", False),
                      ("pid", False)])
            continue
        line = line.split(" ")
        for component in line:
            component = component.split(":")
            if component[0] != "cid":
                d[component[0]] = True
    print(valid)
    return valid


def task2():
    data = get_input_for_day(day)
    # data = get_input_for_file("test")
    valid = 0
    d = dict(
        [("byr", False), ("iyr", False), ("eyr", False), ("hgt", False), ("hcl", False), ("ecl", False),
         ("pid", False)])

    data.append("")
    for line in data:
        if line == "":
            print(d)
            if all(val for val in d.values()):
                valid += 1
            d = dict([("byr", False), ("iyr", False), ("eyr", False), ("hgt", False), ("hcl", False), ("ecl", False),
                      ("pid", False)])
            continue
        line = line.split(" ")
        for component in line:
            component = component.split(":")
            field = component[0]
            value = component[1]
            if field == "byr" and 1920 <= int(value) <= 2002:
                d[field] = True
            elif field == "iyr" and 2010 <= int(value) <= 2020:
                d[field] = True
            elif field == "eyr" and 2020 <= int(value) <= 2030:
                d[field] = True
            elif field == "hgt":
                if not value.endswith(("cm", "in")):
                    continue
                unit = value[-2:]
                value = int(value[0:-2])
                if (unit == "cm" and 150 <= value <= 193) or (unit == "in" and 59 <= value <= 76):
                    d[field] = True
            elif field == "hcl" and re.match("#([a-f]|[0-9]){6}", value):
                d[field] = True
            elif field == "ecl" and value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                d[field] = True
            elif field == "pid" and len(value) == 9:
                d[field] = True

    print(valid)
    return valid


# task1()
task2()
