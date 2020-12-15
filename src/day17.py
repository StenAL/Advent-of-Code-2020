from util import *
import copy
from collections import *

day = 17


def task1():
    data = get_input_for_day(day)
    # data = get_input_for_file("test")
    cycles = 6

    active_cubes = set()
    for i in range(len(data)):
        line = list(data[i])
        for j in range(len(line)):
            if line[j] == "#":
                active_cubes.add((0, i, j))

    for i in range(cycles):
        active_cubes_copy = copy.deepcopy(active_cubes)
        checked_neigbours = set()
        for cube in active_cubes:
            neigbours = get_neigbours(cube)
            active_neigbours = [n for n in neigbours if n in active_cubes]
            if len(active_neigbours) in [2, 3]: # remain active
                pass
            else:  # deactivate
                active_cubes_copy.remove(cube)

            for n in neigbours:
                if n not in active_neigbours and n not in checked_neigbours:
                    n_neigbours = get_neigbours(n)
                    n_active_neigbours = [n for n in n_neigbours if n in active_cubes]
                    if len(n_active_neigbours) == 3:  # activate
                        active_cubes_copy.add(n)
                    checked_neigbours.add(n)
        active_cubes = active_cubes_copy
    ans = len(active_cubes)
    print(ans)
    return ans

def get_neigbours(point):
    x, y, z = point
    r = range(-1, 2)
    neigbours = []
    for x1 in r:
        for y1 in r:
            for z1 in r:
                if x1 != 0 or y1 != 0 or z1 != 0:
                    neigbours.append((x1 + x, y1 + y, z1 + z))
    return neigbours

def get_neigbours2(point):
    x, y, z, w = point
    r = range(-1, 2)
    neigbours = []
    for x1 in r:
        for y1 in r:
            for z1 in r:
                for w1 in r:
                    if x1 != 0 or y1 != 0 or z1 != 0 or w1 != 0:
                        neigbours.append((x1 + x, y1 + y, z1 + z, w1 + w))
    return neigbours

def task2():
    data = get_input_for_day(day)
    # data = get_input_for_file("test")
    cycles = 6

    active_cubes = set()
    for i in range(len(data)):
        line = list(data[i])
        for j in range(len(line)):
            if line[j] == "#":
                active_cubes.add((0, i, j, 0))

    for i in range(cycles):
        active_cubes_copy = copy.deepcopy(active_cubes)
        checked_neigbours = set()
        for cube in active_cubes:
            neigbours = get_neigbours2(cube)
            active_neigbours = [n for n in neigbours if n in active_cubes]
            if len(active_neigbours) in [2, 3]: # remain active
                pass
            else:  # deactivate
                active_cubes_copy.remove(cube)

            for n in neigbours:
                if n not in active_neigbours and n not in checked_neigbours:
                    n_neigbours = get_neigbours2(n)
                    n_active_neigbours = [n for n in n_neigbours if n in active_cubes]
                    if len(n_active_neigbours) == 3:  # activate
                        active_cubes_copy.add(n)
                    checked_neigbours.add(n)
        active_cubes = active_cubes_copy
    ans = len(active_cubes)
    print(ans)
    return ans


# task1()
task2()
