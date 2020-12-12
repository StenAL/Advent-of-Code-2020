import copy

from util import *

day = 11


def task1():
    data = get_input_for_day(day)
    # data = get_input_for_file("test")
    data = [list(line) for line in data]

    change = True
    rows = len(data)
    cols = len(data[0])
    while change:
        change = False
        data_copy = copy.deepcopy(data)
        for row in range(rows):
            for col in range(cols):
                seat = data[row][col]
                row_neighbours = data[max(row - 1, 0):min(row + 2, rows)]
                neighbours = [row_neighbour[max(col - 1, 0):min(col + 2, cols)] for row_neighbour in row_neighbours]
                all_neigbours = "".join(["".join(n) for n in neighbours])
                occupied = all_neigbours.count("#")
                if seat == "#":
                    occupied -= 1
                if seat == "L" and occupied == 0:
                    data_copy[row][col] = "#"
                    change = True
                elif seat == "#" and occupied >= 4:
                    data_copy[row][col] = "L"
                    change = True
        data = data_copy
    ans = 0
    for el in data:
        ans += el.count("#")
    print(ans)
    return ans

def task2():
    data = get_input_for_day(day)
    # data = get_input_for_file("test")
    data = [list(line) for line in data]

    change = True
    rows = len(data)
    cols = len(data[0])

    pairs = []
    pair_sightlines = dict()
    for row in range(rows):
        for col in range(cols):
            pairs.append((row, col))

    for pair in pairs:
        row, col = pair
        print(pair)
        seat = data[row][col]
        if seat == ".":
            continue

        sorted_pairs = sorted(pairs, key=lambda x: abs(row - x[0]) + abs(col - x[1]))
        lu = []
        ru = []
        rd = []
        ld = []
        u = []
        d = []
        l = []
        r = []
        for i in range(1, len(sorted_pairs)):
            x, y = sorted_pairs[i]
            dx = (x - row)
            dy = (y - col)
            if dx == dy:
                if dx < 0:
                    lu.append(sorted_pairs[i])
                elif dx > 0:
                    rd.append(sorted_pairs[i])
            elif dx + dy == 0:
                if dx < 0:
                    ru.append(sorted_pairs[i])
                elif dx > 0:
                    ld.append(sorted_pairs[i])
            elif dy == 0:
                if dx < 0:
                    l.append(sorted_pairs[i])
                elif dx > 0:
                    r.append(sorted_pairs[i])
            elif dx == 0:
                if dy < 0:
                    u.append(sorted_pairs[i])
                elif dy > 0:
                    d.append(sorted_pairs[i])
        pair_sightlines[pair] = [lu, ru, rd, ld, u, d, l, r]

    c = 0
    while change:
        print("c", c)
        change = False
        data_copy = copy.deepcopy(data)

        for pair in pairs:
            row, col = pair
            seat = data[row][col]
            if seat == ".":
                continue
            lu, ru, rd, ld, u, d, l, r = pair_sightlines[pair]
            di = dict([("lu", -1), ("ru", -1), ("ld", -1), ("rd", -1), ("u", -1), ("l", -1), ("d", -1), ("r", -1)])

            for entry in lu:
                contents = data[entry[0]][entry[1]]
                if contents == "#":
                    di["lu"] = 1
                    break
                elif contents == "L":
                    di["lu"] = 0
                    break

            for entry in ru:
                contents = data[entry[0]][entry[1]]
                if contents == "#":
                    di["ru"] = 1
                    break
                elif contents == "L":
                    di["ru"] = 0
                    break
            for entry in rd:
                contents = data[entry[0]][entry[1]]
                if contents == "#":
                    di["rd"] = 1
                    break
                elif contents == "L":
                    di["rd"] = 0
                    break
            for entry in ld:
                contents = data[entry[0]][entry[1]]
                if contents == "#":
                    di["ld"] = 1
                    break
                elif contents == "L":
                    di["ld"] = 0
                    break
            for entry in u:
                contents = data[entry[0]][entry[1]]
                if contents == "#":
                    di["u"] = 1
                    break
                elif contents == "L":
                    di["u"] = 0
                    break
            for entry in d:
                contents = data[entry[0]][entry[1]]
                if contents == "#":
                    di["d"] = 1
                    break
                elif contents == "L":
                    di["d"] = 0
                    break

            for entry in l:
                contents = data[entry[0]][entry[1]]
                if contents == "#":
                    di["l"] = 1
                    break
                elif contents == "L":
                    di["l"] = 0
                    break
            for entry in r:
                contents = data[entry[0]][entry[1]]
                if contents == "#":
                    di["r"] = 1
                    break
                elif contents == "L":
                    di["r"] = 0
                    break

            visible = sum([val for val in di.values() if val == 1])
            if seat == "L" and visible == 0:
                data_copy[row][col] = "#"
                change = True
            elif seat == "#" and visible >= 5:
                data_copy[row][col] = "L"
                change = True
        data = data_copy
        # for line in data:
        #     print("".join(line))
        # print()
        c += 1

    ans = 0
    for el in data:
        ans += el.count("#")
    print(ans)
    return ans

# task1()
task2()
