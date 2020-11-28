def get_input_for_day(day):
    f = open("input/input_" + str(day) + ".txt")
    return [line.strip() for line in f.readlines()]


def get_input_for_file(file):
    f = open("input/input_" + file + ".txt")
    return [line.strip() for line in f.readlines()]
