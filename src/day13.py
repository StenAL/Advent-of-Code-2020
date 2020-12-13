import math

from util import *

day = 13


def task1():
    data = get_input_for_day(day)
    # data = get_input_for_file("test")
    depart = int(data[0])
    buses = [int(bus) for bus in data[1].split(",") if bus != "x"]

    quotients = [depart // bus for bus in buses]
    next_departures = [(quotients[i] + 1) * buses[i] for i in range(len(quotients))]

    first_departure = min(next_departures)
    bus_id = buses[next_departures.index(first_departure)]
    wait = first_departure - depart

    ans = bus_id * wait
    print(ans)
    return ans


def task2():
    data = get_input_for_day(day)
    data = get_input_for_file("test")
    data = [bus for bus in data[1].split(",")]
    buses = [int(bus) for bus in data if bus != "x"]
    offsets = [data.index(str(bus)) for bus in buses]
    combined_equations = [] # list of (b, a) where answers is in the form of ax + b
    for i in range(0, len(buses) - 1):
        for j in range(i + 1, len(buses)):

            b1 = buses[i]
            b2 = buses[j]
            k = 0
            while True:
                if k % b1 == (b1 - offsets[i]) % b1 and k % b2 == (b2 - offsets[j]) % b2:
                    combined_equations.append((k, b1 * b2))
                    break
                k += 1

    # 3417 = 17 * a + 13 * b - 2 + 19 * c + 3 == 17a + 13b + 19c + 5
    # 17a = x
    # 13b - 2 = x
    # 19c - 3 = x

    # x mod 17 = 0
    # x mod 13 = 13 - 2 = 11
    # x mod 19 = 19 - 3 = 16

    while len(combined_equations) > 1:
        new_equations = []
        for i in range(0, len(combined_equations) - 1, 1):

            b1 = combined_equations[i][0]
            b2 = combined_equations[i + 1][0]
            increment1 = combined_equations[i][1]
            increment2 = combined_equations[i + 1][1]
            if b1 >= b2:
                k = b1
                increment = increment1
            else:
                k = b2
                increment = increment2
            # print(f"{b1}a + {increment1}, {b2}a + {increment2}")
            while True:
                if (k - b1) % increment1 == 0 and (k - b2) % increment2 == 0:
                    l = lcm(increment1, increment2)
                    new_equations.append((k, l))
                    # print(f"=== {l}a + {k}, \n")
                    break
                k += increment
        combined_equations = new_equations

    ans = combined_equations[0][0]
    print(ans)
    return ans


def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)


# task1()
task2()
