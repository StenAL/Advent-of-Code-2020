from util import *

day = 12


def task1():
    data = get_input_for_day(day)
    # data = get_input_for_file("test")
    clockwise = ["N", "E", "S", "W"]
    n = 0
    e = 0
    facing = "E"
    for line in data:
        command = line[0]
        value = int(line[1:])
        if command == "F":
            command = facing
        elif command == "R":
            facing = clockwise[(clockwise.index(facing) + int(value/90)) % len(clockwise)]
            continue
        elif command == "L":
            facing = clockwise[(clockwise.index(facing) - int(value/90)) % len(clockwise)]
            continue

        if command == "N":
            n += value
        elif command == "E":
            e += value
        elif command == "S":
            n -= value
        elif command == "W":
            e -= value
    ans = (abs(e) + abs(n))
    print(ans)
    return ans



def task2():
    data = get_input_for_day(day)
    # data = get_input_for_file("test")
    n = 0
    e = 0
    waypoint_n = 1
    waypoint_e = 10
    for line in data:
        command = line[0]
        value = int(line[1:])
        if command == "F":
            n += waypoint_n * value
            e += waypoint_e * value
        elif command == "R":
            for i in range(int(value/90)):
                tmp = waypoint_e
                waypoint_e = waypoint_n
                waypoint_n = -1 * tmp
            continue
        elif command == "L":
            for i in range(int(value/90)):
                tmp = waypoint_n
                waypoint_n = waypoint_e
                waypoint_e = -1 * tmp
            continue
        if command == "N":
            waypoint_n += value
        elif command == "E":
            waypoint_e += value
        elif command == "S":
            waypoint_n -= value
        elif command == "W":
            waypoint_e -= value

    ans = (abs(e) + abs(n))
    print(ans)
    return ans


# task1()
task2()
