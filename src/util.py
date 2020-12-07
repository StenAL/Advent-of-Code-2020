def get_input_for_day(day):
    f = open("input/day" + str(day) + ".txt")
    return [line.strip() for line in f.readlines()]


def get_int_input_for_day(day):
    f = open("input/day" + str(day) + ".txt")
    return [int(line.strip()) for line in f.readlines()]


def get_input_for_file(file):
    f = open("input/" + file + ".txt")
    return [line.strip() for line in f.readlines()]


def get_int_input_for_file(file):
    f = open("input/" + file + ".txt")
    return [int(line.strip()) for line in f.readlines()]
