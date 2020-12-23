from timeit import default_timer as timer
from util import *
from collections import *
import copy
import itertools

day = 23


def task1():
    data = get_input_for_day(day)
    # data = get_input_for_file("test")
    cups = [int(n) for n in data[0]]
    cups_len = len(cups)
    current_cup_index = 0
    current_cup = cups[current_cup_index]
    iterations = 100
    for i in range(iterations):
        # print(f"{i}: ({current_cup})", "cups", cups)
        next_cups = []
        next_cup_indices = []
        for j in range(3):
            next_cup_indices.append((current_cup_index + j + 1) % cups_len)
            next_cups.append(cups[(current_cup_index + j + 1) % cups_len])
        # print("pick up", next_cups)

        target_cup = (current_cup - 1) % (cups_len + 1)
        while target_cup in next_cups or target_cup == 0:
            target_cup = (target_cup - 1) % (cups_len + 1)
        target_cup_index = cups.index(target_cup)
        # print("dest", target_cup)

        new_cups = [target_cup] + next_cups
        skip_cups = False
        for j in range(1, cups_len-3):
            k = (target_cup_index + j) % cups_len
            if k in next_cup_indices:
                skip_cups = True
            if skip_cups:
                k += 3
            k = k % cups_len
            # print(k)
            new_cups.append(cups[k])
        # print("new", new_cups, "\n")
        current_cup = cups[(current_cup_index + 4) % cups_len]
        cups = new_cups
        current_cup_index = cups.index(current_cup)

    one_index = cups.index(1)
    ans = []
    for i in range(1, cups_len):
        ans.append(str(cups[(one_index + i) % cups_len]))
    ans = "".join(ans)
    print(ans)
    return ans


def task2():
    data = get_input_for_day(day)
    # data = get_input_for_file("test")
    data = [int(n) for n in data[0]]
    elements = 1000000
    next = [-1] * (elements + 1)
    for i in range(len(data) - 1):
        cup = data[i]
        next[cup] = data[(i + 1)]
    next[data[-1]] = 10

    for i in range(10, elements + 1):
        next[i] = i + 1
    next[-1] = data[0]
    iterations = 10000000
    current_cup = data[0]
    for i in range(iterations):
        if i % 1000000 == 0:
            print(i)
        next1 = next[current_cup]
        next2 = next[next1]
        next3 = next[next2]
        next_cups = [next1, next2, next3]

        target_cup = (current_cup - 1) % (elements + 1)
        while target_cup in next_cups or target_cup == 0:
            target_cup = (target_cup - 1) % (elements + 1)

        tmp = next[target_cup]
        next[current_cup] = next[next3]
        next[target_cup] = next1
        next[next3] = tmp
        current_cup = next[current_cup]


    next1 = next[1]
    next2 = next[next1]
    ans = next1 * next2
    print(ans)
    return ans

# task1()
task2()
