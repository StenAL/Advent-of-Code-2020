from util import *


def task1():
    data = get_input_for_day(2)
    correct = 0
    for line in data:
        counts, letter, password = line.split(" ")
        letter = letter[0]
        minimum, maximum = [int(n) for n in counts.split("-")]
        c = password.count(letter)
        if minimum <= c <= maximum:
            correct += 1
    # print(correct)
    return correct


def task2():
    data = get_input_for_day(2)
    correct = 0
    for line in data:
        indices, letter, password = line.split(" ")
        letter = letter[0]
        index1, index2 = [int(n) - 1 for n in indices.split("-")]
        pos1 = int(password[index1] == letter)
        pos2 = int(password[index2] == letter)
        correct += pos1 ^ pos2
    # print(correct)
    return correct

# task1()
# task2()
