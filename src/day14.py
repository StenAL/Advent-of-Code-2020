from util import *

day = 14


def task1():
    data = get_input_for_day(day)
    # data = get_input_for_file("test")
    ones = []
    zeroes = []
    mem = dict()
    for line in data:
        line = line.split(" = ")
        # print(line[0])
        if line[0] == "mask":
            mask = line[1]
            ones = [i for i in range(len(mask)) if mask[i] == "1"]
            zeroes = [i for i in range(len(mask)) if mask[i] == "0"]
        else:
            address = line[0][4:-1]
            val = line[1]
            val = "{0:08b}".format(int(val))
            val = val.zfill(36)
            for i in ones:
                val = val[:i] + "1" + val[i + 1:]
            for i in zeroes:
                val = val[:i] + "0" + val[i + 1:]
            mem[address] = val

    ans = sum([int(val, 2) for val in mem.values()])
    print(ans)
    return ans


def task2():
    data = get_input_for_day(day)
    # data = get_input_for_file("test")
    ones = []
    floats = []
    mem = dict()
    for line in data:
        line = line.split(" = ")
        if line[0] == "mask":
            mask = line[1]
            ones = [i for i in range(len(mask)) if mask[i] == "1"]
            floats = [i for i in range(len(mask)) if mask[i] == "X"]
        else:
            address = line[0][4:-1]
            val = line[1]
            address = "{0:08b}".format(int(address))
            address = address.zfill(36)
            for i in ones:
                address = address[:i] + "1" + address[i + 1:]
            addresses = get_floats(address, floats)
            for a in addresses:
                mem[int(a,2)] = val

    ans = sum([int(val) for val in mem.values()])
    print(ans)
    return ans

def get_floats(address, floats):
    if len(floats) == 0:
        return [address]

    i = floats[0]
    a0 = address[:i] + "0" + address[i + 1:]
    a1 = address[:i] + "1" + address[i + 1:]
    return get_floats(a0, floats[1:]) + get_floats(a1, floats[1:])


# task1()
task2()
