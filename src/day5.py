from util import *

day = 5


def task1():
    data = get_input_for_day(day)
    # data = get_input_for_file("test")
    max_id = 0
    for seat in data:
        row_data = seat[0:7]
        seat_data = seat[7:]
        min_row = 1
        max_row = 128
        row_range = 128
        for s in row_data:
            if s == "F":
                max_row = max_row - row_range/2
            else:
                min_row = min_row + row_range/2
            row_range = row_range/2
        row = min_row - 1

        min_seat = 1
        max_seat = 8
        seat_range = 8
        for s in seat_data:
            if s == "L":
                max_seat = max_seat - seat_range/2
            else:
                min_seat = min_seat + seat_range/2
            seat_range = seat_range/2
        seat = min_seat - 1

        ans = int(row * 8 + seat)
        max_id = max(max_id, ans)

    print(max_id)
    return max_id


def task2():
    data = get_input_for_day(day)
    # data = get_input_for_file("test")
    ids = []
    for seat in data:
        row_data = seat[0:7]
        seat_data = seat[7:]
        min_row = 1
        max_row = 128
        row_range = 128
        for s in row_data:
            if s == "F":
                max_row = max_row - row_range / 2
            else:
                min_row = min_row + row_range / 2
            row_range = row_range / 2
        row = min_row - 1

        min_seat = 1
        max_seat = 8
        seat_range = 8
        for s in seat_data:
            if s == "L":
                max_seat = max_seat - seat_range / 2
            else:
                min_seat = min_seat + seat_range / 2
            seat_range = seat_range / 2
        seat = min_seat - 1

        ans = int(row * 8 + seat)
        ids.append(ans)

    ids.sort()
    ans = 0
    for i in range(len(ids) - 1):
        el = ids[i]
        if ids[i + 1] != el + 1:
            ans = el + 1
            break

    print(ans)
    return ans


# task1()
task2()
