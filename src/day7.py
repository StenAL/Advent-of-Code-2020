from util import *

day = 7


def task1():
    data = get_input_for_day(day)
    # data = get_input_for_file("test")
    d = dict()
    for line in data:
        outer, inner = line.split(" contain ")
        outer = " ".join(outer.split(" ")[0:2])
        inner = inner.split(", ")
        d[outer] = []

        for inner_bag in inner:
            inner_bag = " ".join(inner_bag.split(" ")[1:3])
            d[outer].append(inner_bag)

    ans = 0
    target = ["shiny gold"]
    done = set()
    while len(target) != 0:
        new_target = []
        for item in d.items():
            if any([t for t in target if t in item[1] and item[0] not in done]):
                new_target.append(item[0])

        done = done.union(target)
        target = [el for el in new_target if el not in done]
        ans += len(target)
    print(ans)
    return ans


def task2():
    data = get_input_for_day(day)
    # data = get_input_for_file("test")
    d = dict()
    for line in data:
        outer, inner = line.split(" contain ")
        outer = " ".join(outer.split(" ")[0:2])
        inner = inner.split(", ")
        d[outer] = []

        for inner_bag in inner:
            inner_bag = " ".join(inner_bag.split(" ")[0:3])
            if inner_bag == "no other bags.":
                continue
            d[outer].append(inner_bag)

    ans = 0
    target = ["1 shiny gold"]
    while len(target) != 0:
        new_target = []
        for item in target:
            item = item.split(' ')
            count = int(item[0])
            colour = " ".join(item[1:])
            contains = d[colour]
            for bag in contains:
                split_bag = bag.split(" ")
                new_count = int(split_bag[0]) * count
                ans += new_count
                new_target.append(" ".join([str(new_count)] + split_bag[1:]))

        target = new_target
    print(ans)
    return ans

# task1()
task2()
