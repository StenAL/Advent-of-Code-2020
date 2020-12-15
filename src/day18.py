import re

from util import *
from collections import *
import copy

day = 18


def task1():
    data = get_input_for_day(day)
    # data = get_input_for_file("test")
    ans = 0
    for line in data:
        line = line.replace(" ", "")
        val = evaluate(line)
        ans += val
    print(ans)
    return ans

def evaluate(expr):
    operator = "+"
    acc = 0
    nest = 0
    for i in range(len(expr)):
        symbol = expr[i]
        if symbol == "(":
            nest += 1
            if nest == 1:
                nested_val = evaluate(expr[i+1:])
                if operator == "*":
                    acc *= nested_val
                else:
                    acc += nested_val
        elif symbol == ")":
            if nest == 0:
                return acc
            nest -= 1
            continue
        if nest > 0:
            continue
        if symbol == "+":
            operator = "+"
        elif symbol == "*":
            operator = "*"
        else:  # number
            num = int(symbol)
            if operator == "*":
                acc *= num
            else:
                acc += num
    return acc




def task2():
    data = get_input_for_day(day)
    # data = get_input_for_file("test")
    data = ["(" + line.replace("(", "((").replace(")", "))").replace(" * ", ") * (") + ")" for line in data]
    ans = 0
    for line in data:
        line = line.replace(" ", "")
        val = evaluate(line)
        ans += val
    print(ans)
    return ans



# task1()
task2()
