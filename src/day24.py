from util import *
from collections import *
import copy

day = 24


def task1():
    data = get_input_for_day(day)
    # data = get_input_for_file("test")
    black = set()
    for line in data:
        x = 0
        y = 0
        line = list(line)
        directions = []
        if line[0] in ["e", "w"]:
            directions.append(line[0])
        for i in range(1, len(line)):
            if line[i] in ["e", "w"] and line[i - 1] in ["s", "n"]:
                directions.append(line[i - 1] + line[i])
            elif line[i] in ["e", "w"]:
                directions.append(line[i])
        for direction in directions:
            if direction == "e":
                x += 1
            elif direction == "w":
                x -= 1
            elif direction == "ne":
                x += 0.5
                y += 0.5
            elif direction == "se":
                x += 0.5
                y -= 0.5
            elif direction == "nw":
                x -= 0.5
                y += 0.5
            elif direction == "sw":
                x -= 0.5
                y -= 0.5
        if (x, y) not in black:
            black.add((x, y))
        else:
            black.remove((x, y))
    ans = len(black)
    print(ans)
    return ans


def task2():
    data = get_input_for_day(day)
    # data = get_input_for_file("test")
    black = set()
    for line in data:
        x = 0
        y = 0
        line = list(line)
        directions = []
        if line[0] in ["e", "w"]:
            directions.append(line[0])
        for i in range(1, len(line)):
            if line[i] in ["e", "w"] and line[i - 1] in ["s", "n"]:
                directions.append(line[i - 1] + line[i])
            elif line[i] in ["e", "w"]:
                directions.append(line[i])
        for direction in directions:
            if direction == "e":
                x += 1
            elif direction == "w":
                x -= 1
            elif direction == "ne":
                x += 0.5
                y += 0.5
            elif direction == "se":
                x += 0.5
                y -= 0.5
            elif direction == "nw":
                x -= 0.5
                y += 0.5
            elif direction == "sw":
                x -= 0.5
                y -= 0.5
        if (x, y) not in black:
            black.add((x, y))
        else:
            black.remove((x, y))

    iterations = 100
    for i in range(iterations):
        checked_neigbours = set()
        black_copy = set()
        for tile in black:
            x, y = tile
            neigbours = get_neigbours(x, y)
            intersection = black.intersection(neigbours)
            if len(intersection) == 0 or len(intersection) > 2: # flip white
                pass
            else:
                black_copy.add(tile)
            for neigbour in neigbours:
                if neigbour in checked_neigbours or neigbour in black:
                    continue
                x1, y1 = neigbour
                neigbours1 = get_neigbours(x1, y1)
                intersection1 = black.intersection(neigbours1)
                if len(intersection1) == 2:  # flip black
                    black_copy.add(neigbour)
                checked_neigbours.add(neigbour)
        black = black_copy
    ans = len(black)
    print(ans)
    return ans

def get_neigbours(x, y):
    e = (x + 1, y)
    w = (x - 1, y)
    ne = (x + 0.5, y + 0.5)
    se = (x + 0.5, y - 0.5)
    nw = (x - 0.5, y + 0.5)
    sw = (x - 0.5, y - 0.5)
    return [e, w, ne, se, nw, sw]

# task1()
task2()
