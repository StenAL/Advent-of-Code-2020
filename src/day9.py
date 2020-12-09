from util import *

day = 9


def task1():
    data = get_int_input_for_day(day)
    # data = get_int_input_for_file("test")
    preamble_length = 25
    preamble = set(data[:preamble_length])
    for i in range(preamble_length, len(data)):
        number = data[i]
        found = False
        for p in preamble:
            if number - p in preamble:
                preamble.remove(data[i - preamble_length])
                preamble.add(number)
                found = True
                break
        if not found:
            ans = number
            print(ans)
            return ans


def task2():
    data = get_int_input_for_day(day)
    # data = get_int_input_for_file("test")
    target = 22406676
    s = data[0]
    window_start = 0
    for window_end in range(1, len(data)):
        n = data[window_end]
        s += n
        while s > target:
            s -= data[window_start]
            window_start += 1
        if s == target:
            window = data[window_start:window_end + 1]
            ans = min(window) + max(window)
            print(ans)
            return ans
            break



# task1()
task2()
