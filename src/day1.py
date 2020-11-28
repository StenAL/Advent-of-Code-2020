from util import *

def task1():
    input = get_input_for_day(1)
    input = [int(n) for n in input]
    input.sort()
    for a in input:
        for b in input:
            sum = a + b
            if sum == 2020:
                print(f"a={a} b={b}, ans={a*b}")
                return
            elif sum > 2020:
                break

def task2():
    input = get_input_for_day(1)
    input = [int(n) for n in input]
    input.sort()
    for a in input:
        for b in input:
            sum1 = a + b
            if sum1 > 2020:
                break

            for c in input:
                sum2 = sum1 + c
                if sum2 == 2020:
                    print(f"a={a} b={b} c={c}, ans={a*b*c}")
                    return
                elif sum2 > 2020:
                    break

#task1()
# task2()