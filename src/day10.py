from util import *

day = 10


def task1():
    data = get_int_input_for_day(day)
    # data = get_int_input_for_file("test")
    data.sort()
    max_jolts = max(data)
    one_count = 0
    three_count = 1  # final adapter
    current = 0
    for i in range(len(data)):
        next = data[i]
        if next-current == 3:
            three_count += 1
        elif next-current == 1:
            one_count += 1
        current = next

    ans = one_count * three_count
    print(ans)
    return ans


def task2():
    data = get_int_input_for_day(day)
    # data = get_int_input_for_file("test")
    data.sort()
    max_jolts = max(data)
    data.insert(0, 0)
    data.append(max_jolts + 3)

    direct_reach_count = dict()
    for el in data:
        direct_reach = 0
        if (el - 1) in data:
            direct_reach += 1
        if (el - 2) in data:
            direct_reach += 1
        if (el - 3) in data:
            direct_reach += 1
        direct_reach_count[el] = direct_reach
    direct_reach_count[0] = 1

    chain = 0
    chains = []
    for val in direct_reach_count.values():
        if val == 1:
            if chain != 0:
                chains.append(chain - 1)
            chain = 0
        else:
            chain += val

    print(chains)
    ans = 1
    for el in chains:
        if el == 1:
            el = 2
        ans *= el

    print(ans)
    return ans



# task1()
task2()
