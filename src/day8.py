from util import *

day = 8


def task1():
    data = get_input_for_day(day)
    # data = get_input_for_file("test")
    done = set()
    i = 0
    acc = 0
    while i not in done:
        done.add(i)
        line = data[i]
        instruction, argument = line.split(" ")
        argument = int(argument)
        if instruction == "acc":
            acc += argument
            i += 1
        elif instruction == "jmp":
            i += argument
        elif instruction == "nop":
            i += 1
    print(acc)
    return acc


def task2():
    data = get_input_for_day(day)
    # data = get_input_for_file("test")

    for idx in range(len(data)):
        insn, arg = data[idx].split(" ")
        data_copy = data.copy()
        if insn == "nop":
            data_copy[idx] = "jmp " + arg
        elif insn == "jmp":
            data_copy[idx] = "nop " + arg
        else:
            continue


        done = set()
        i = 0
        acc = 0
        while i not in done:
            if i == len(data_copy):
                print(acc)
                return acc
            done.add(i)
            line = data_copy[i]
            instruction, argument = line.split(" ")
            argument = int(argument)
            if instruction == "acc":
                acc += argument
                i += 1
            elif instruction == "jmp":
                i += argument
            elif instruction == "nop":
                i += 1


# task1()
task2()
