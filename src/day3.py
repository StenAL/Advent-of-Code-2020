from util import *

day = 3


def task1():
    data = get_input_for_day(day)
    x = 0
    y = 0
    trees = 0
    while y < len(data):
        content = data[y][x]
        if content == "#":
            trees += 1
        x += 3
        x = x % (len(data[0]))
        y += 1
    return trees

def get_trees(x_slope, y_slope):
    data = get_input_for_day(day)
    x = 0
    y = 0
    trees = 0
    while y < len(data):
        content = data[y][x]
        if content == "#":
            trees += 1
        x += x_slope
        x = x % (len(data[0]))
        y += y_slope
    return trees

def task2():
    a = get_trees(1, 1)
    b = get_trees(3, 1)
    c = get_trees(5, 1)
    d = get_trees(7, 1)
    e = get_trees(1, 2)
    ans = a * b * c * d * e
    print(ans)
    return ans


# task1()
task2()
