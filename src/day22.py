from util import *
from collections import *
import copy

day = 22


def task1():
    data = get_input_for_day(day)
    # data = get_input_for_file("test")
    p1 = []
    p2 = []
    segment = 0
    for line in data:
        if line == "":
            segment += 1
            continue
        if line.startswith("Player"):
            continue
        if segment == 0:
            p1.append(int(line))
        else:
            p2.append(int(line))

    total_cards = len(p1) + len(p2)

    while True:
        p1_card = p1.pop(0)
        p2_card = p2.pop(0)
        if p1_card > p2_card:
            p1 += [p1_card, p2_card]
        else:
            p2 += [p2_card, p1_card]
        if len(p1) == total_cards:
            winner = p1
            break
        elif len(p2) == total_cards:
            winner = p2
            break

    ans = 0
    for i in range(len(winner)):
        card = winner[len(winner) - 1 - i]
        ans += card * (i + 1)
    print(ans)
    return ans


def task2():
    data = get_input_for_day(day)
    # data = get_input_for_file("test")
    p1 = []
    p2 = []
    segment = 0
    for line in data:
        if line == "":
            segment += 1
            continue
        if line.startswith("Player"):
            continue
        if segment == 0:
            p1.append(int(line))
        else:
            p2.append(int(line))

    winner, result = game(p1, p2, 1)
    ans = 0
    for i in range(len(result)):
        card = result[len(result) - 1 - i]
        ans += card * (i + 1)
    print(ans)
    return ans

def game(p1, p2, level):
    played_configurations = set()
    total_cards = len(p1) + len(p2)
    while True:
        if (str(p1), str(p2)) in played_configurations:
            return 1, p1
        played_configurations.add((str(p1), str(p2)))

        p1_card = p1.pop(0)
        p2_card = p2.pop(0)
        if len(p1) >= p1_card and len(p2) >= p2_card:
            result = game(p1[:p1_card], p2[:p2_card], level + 1)
            if result[0] == 1:
                p1 += [p1_card, p2_card]
            else:
                p2 += [p2_card, p1_card]
        elif p1_card > p2_card:
            p1 += [p1_card, p2_card]
        else:
            p2 += [p2_card, p1_card]
        if len(p1) == total_cards:
            return 1, p1
        elif len(p2) == total_cards:
            return 2, p2


# task1()
task2()
