import re

from util import *
from collections import *
import copy
import itertools

day = 19


def task1():
    data = get_input_for_day(day)
    # data = get_input_for_file("test")
    rules = dict()
    memo = dict()
    ans = 0
    section = 0
    for line in data:
        if line == "":
            section += 1
            evaluate(0, rules, memo)
            continue
        if section == 0:
            head, body = line.split(": ")
            head = int(head)
            if body.startswith("\"") and body.endswith("\""):
                rules[head] = body[1]
            else:
                if "|" in body:
                    body = body.split("|")
                    body = [part.strip().split(" ") for part in body]
                    body = [[int(n) for n in part] for part in body]
                else:
                    body = body.split(" ")
                    body = [[int(n) for n in body]]
                rules[head] = body
        else:
            if line in memo[0]:
                ans += 1

    print(ans)
    return ans


def task2():
    data = get_input_for_day(day)
    # data = get_input_for_file("test")
    rules = dict()
    memo = dict()
    ans = 0
    section = 0
    for line in data:
        if line == "":
            section += 1
            evaluate(42, rules, memo)
            evaluate(31, rules, memo)
            continue
        if section == 0:
            head, body = line.split(": ")
            head = int(head)
            if head == 8:
                body = "X"  # X = 42+
                rules[head] = body
                continue
            if head == 11:
                body = "Y"  # Y = 42^i 31^i -- not regular
                rules[head] = body
                continue

            if body.startswith("\"") and body.endswith("\""):
                rules[head] = body[1]
            else:
                if "|" in body:
                    body = body.split("|")
                    body = [part.strip().split(" ") for part in body]
                    body = [[int(n) for n in part] for part in body]
                else:
                    body = body.split(" ")
                    body = [[int(n) for n in body]]
                rules[head] = body
        else:
            # pattern -- 42^i 31^j where i >= j; i > 0, j > 0
            parts = [line[i:i + 8] for i in range(0, len(line), 8)]
            # parts = [line[i:i + 5] for i in range(0, len(line), 5)]  # test has parts of len 5
            j = 0
            for part in reversed(parts):
                if part in memo[31]:
                    j += 1
                else:
                    break
            i = 0
            for part in parts:
                if part in memo[42]:
                    i += 1
                else:
                    break
            if i > 0 and j > 0 and i > j and i + j >= len(parts):
                ans += 1


    print(ans)
    return ans


def evaluate(head, d, existing):
    if head in existing:
        return existing[head]
    body = d[head]
    if type(body) == str:
        s = set()
        s.add(body)
        existing[head] = s
        return s
    matches = set()
    for choice in body:
        match = []
        for el in choice:
            m = evaluate(el, d, existing)
            match.append(m)
        x = set(itertools.product(*match))
        for el in x:
            el = "".join(el)
            matches.add(el)
    existing[head] = matches
    return matches

# task1()
task2()
