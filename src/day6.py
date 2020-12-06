from util import *

day = 6


def task1():
    data = get_input_for_day(day)
    # data = get_input_for_file("test")
    data.append("")
    group_answers = set()
    ans = 0
    for line in data:
        if line == "":
            ans += len(group_answers)
            group_answers = set()
            continue

        for el in line:
            group_answers.add(el)

    print(ans)
    return ans


def task2():
    data = get_input_for_day(day)
    # data = get_input_for_file("test")
    data.append("")
    group_answers = set()
    individual_answers = []
    ans = 0
    for line in data:
        if line == "":
            for el in group_answers:
                if all(individual_answer.__contains__(el) for individual_answer in individual_answers):
                    ans += 1
            group_answers = set()
            individual_answers = []
            continue

        for el in line:
            group_answers.add(el)
        individual_answers.append(line)

    print(ans)
    return ans

# task1()
task2()
