from util import *
from collections import *
import copy

day = 25


def task1():
    data = get_input_for_day(day)
    # data = get_input_for_file("test")
    pu1 = int(data[0])
    pu2 = int(data[1])
    initial = 1
    value = initial
    subject = 7
    i = 1
    while True:
        value = value * subject
        value = value % 20201227
        if value == pu1 or value == pu2:
            broken_key = value
            break
        i += 1

    if pu1 == broken_key:
        key = pu2
    else:
        key = pu1

    subject = key
    value = initial
    for j in range(i):
        value = value * subject
        value = value % 20201227

    print(value)


def task2():
    print("free real estate")
    return


task1()
task2()
