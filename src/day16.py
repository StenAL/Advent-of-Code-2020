from util import *
from collections import *

day = 16


def task1():
    data = get_input_for_day(day)
    # data = get_input_for_file("test")
    data.append("")
    section = 0
    ranges = []
    ans = 0
    for line in data:
        if line == "":
            section += 1
            continue
        if section == 0:
            line = line.split(": ")
            line_ranges = line[1].split(" or ")
            lower_range = [int(n) for n in line_ranges[0].split("-")]
            upper_range = [int(n) for n in line_ranges[1].split("-")]

            ranges.append((lower_range, upper_range))
        if section == 1:
            continue
        if section == 2 and line != "nearby tickets:":
            values = [int(n) for n in line.split(",")]
            for value in values:
                valid = False
                for r in ranges:
                    r1, r2 = r
                    if r1[0] <= value <= r1[1] or r2[0] <= value <= r2[1]:
                        valid = True
                        break
                if not valid:
                    ans += value
    print(ans)
    return ans


def task2():
    data = get_input_for_day(day)
    # data = get_input_for_file("test2")
    data.append("")
    section = 0
    ranges = []
    valid_tickets = []
    field_names = []
    my_ticket = []
    for line in data:
        if line == "":
            section += 1
            continue
        if section == 0:
            line = line.split(": ")
            field_names.append(line[0])
            line_ranges = line[1].split(" or ")
            lower_range = [int(n) for n in line_ranges[0].split("-")]
            upper_range = [int(n) for n in line_ranges[1].split("-")]

            ranges.append((lower_range, upper_range))
        if section == 1 and line != "your ticket:":
            my_ticket = [int(n) for n in line.split(",")]
        if section == 2 and line != "nearby tickets:":
            values = [int(n) for n in line.split(",")]
            ticket_valid = True
            for value in values:
                value_valid = False
                for r in ranges:
                    r1, r2 = r
                    if r1[0] <= value <= r1[1] or r2[0] <= value <= r2[1]:
                        value_valid = True
                        break
                if not value_valid:
                    ticket_valid = False
            if ticket_valid:
                valid_tickets.append(values)

    field_candidates = [[] for _ in range(len(ranges))]
    for i in range(len(ranges)):
        r1, r2 = ranges[i]
        for j in range(len(ranges)):
            match = all([r1[0] <= ticket[j] <= r1[1] or r2[0] <= ticket[j] <= r2[1] for ticket in valid_tickets])
            if match:
                field_candidates[i].append(j)

    fields = [-1] * len(ranges)
    while any([len(f) > 0 for f in field_candidates]):
        correct_field = [f for f in field_candidates if len(f) == 1][0]
        i = field_candidates.index(correct_field)
        j = correct_field[0]
        fields[i] = j
        for f in field_candidates:
            if j in f:
                f.remove(j)

    sorted_field_names = [x for _, x in sorted(zip(fields, field_names))]
    ans = 1
    for i in range(len(sorted_field_names)):
        name = sorted_field_names[i]
        if name.startswith("departure"):
            ans *= my_ticket[i]
    print(ans)
    return ans


# task1()
task2()
