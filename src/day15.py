from util import *
from collections import *

day = 15


def task1():
    data = get_input_for_day(day)
    # data = get_input_for_file("test")
    data = data[0].split(",")
    most_recently_said = defaultdict(list)
    prev = 0
    for i in range(len(data)):
        num = int(data[i])
        most_recently_said[num].append(i + 1)
        prev = num

    turns = 2020
    for i in range(len(data) + 1, turns + 1):
        # print("Turn ", i)
        prev_timestamps = most_recently_said[prev]
        # print("previous number:", prev, "said at" , last_timestamps)
        if len(prev_timestamps) == 1:
            num = 0
        else:
            num = prev_timestamps[-1] - prev_timestamps[-2]
        most_recently_said[num].append(i)
        prev = num

    ans = prev
    print(ans)
    return ans



def task2():
    data = get_input_for_day(day)
    # data = get_input_for_file("test")
    data = data[0].split(",")
    most_recently_said = defaultdict(list)
    prev = 0
    for i in range(len(data)):
        num = int(data[i])
        most_recently_said[num].append(i + 1)
        prev = num

    turns = 30000000
    for i in range(len(data) + 1, turns + 1):
        if i % 1000000 == 0:
            print("Turn ", i)
        prev_timestamps = most_recently_said[prev]
        # print("previous number:", prev, "said at" , last_timestamps)
        if len(prev_timestamps) == 1:
            num = 0
        else:
            num = prev_timestamps[-1] - prev_timestamps[-2]
        most_recently_said[num].append(i)
        prev = num

    ans = prev
    print(ans)
    return ans




# task1()
task2()
