# import stuff
from typing import List
from collections import Counter

# define some functions

# class to hold all the seats in the waiting area grid
WaitingArea = List[List[str]]

# object to hold relative coordinates for all neighbouring seats 
neighbors = [(-1, -1), (-1, 0),  (-1, 1),
             ( 0, -1),            (0, 1),
             ( 1, -1), ( 1, 0),   (1, 1)]

# function to parse input into waiting area
def parse(raw: str) -> WaitingArea:
    return [list(row) for row in raw.split('\n')]

# ----------------- PART 1 -----------------------

def next_value(wa: WaitingArea, i: int, j:int) -> str:
    """
    Given a waiting area and coordinates for the seat,
    determine whether the new status for the seat once 
    passengers arrive.
    """

    # measure number of columns and rows in the grid
    num_rows = len(wa)
    num_cols = len(wa[0])

    # count all values in neighbouring seats
    counts = Counter(
        wa[i + di][j + dj]
        for di, dj in neighbors
        if 0 <= i + di < num_rows and 0 <= j + dj < num_cols
    )

    seat = wa[i][j]

    # empty seats without neighbours become occupied
    if seat == 'L' and counts['#'] == 0:
        return '#'

    # occupied seats with 4 or more neighbors become free
    if seat == '#' and counts['#'] >= 4:
        return 'L'

    # otherwise, do not change
    else:
        return seat


def step(wa: WaitingArea) -> WaitingArea:
    """
    Updates WaitingArea seat status based on rules
    for seating.
    """
    return [
        [
            next_value(wa, i, j)
            for j, col in enumerate(row)
        ]
        for i, row in enumerate(wa)
    ]

def final_seating(wa: WaitingArea) -> int:
    """
    Keeps updatiing WaitingArea according to the seat
    rules until no more changes occur. Returns the
    total number of occupied seats.
    """

    # keep updating waiting area until no more changes
    while True:
        next_wa = step(wa)
        if next_wa == wa: break
        else: wa = next_wa

    # return sum of occupied seats in final waiting area    
    return sum(seat == '#' for row in wa for seat in row)

# ----------------- PART 2 -----------------------

def first_seat(wa: WaitingArea, i: int, j:int, di:int, dj: int) -> str:
    """
    Given a waiting area, coordinates for the seat,
    and a direction to look, determine whether the 
    person sitting in the seat can see other occupied seats.
    """

    # measure number of columns and rows in the grid
    num_rows = len(wa)
    num_cols = len(wa[0])

    while True:
        i += di
        j += dj

        if 0 <= i < num_rows and 0 <= j < num_cols:
            seat = wa[i][j]
            if seat == '#' or seat == 'L':
                return seat
        else:
            return '.'


def next_value2(wa: WaitingArea, i: int, j:int) -> str:
    """
    Given a waiting area and coordinates for the seat,
    determine whether the new status for the seat once 
    passengers arrive.
    """

    # count all values in neighbouring seats
    counts = Counter(
        first_seat(wa, i, j, di, dj)
        for di, dj in neighbors
    )

    seat = wa[i][j]

    # empty seats without neighbours become occupied
    if seat == 'L' and counts['#'] == 0:
        return '#'

    # occupied seats with 4 or more neighbors become free
    if seat == '#' and counts['#'] >= 5:
        return 'L'

    # otherwise, do not change
    else:
        return seat


def step2(wa: WaitingArea) -> WaitingArea:
    """
    Updates WaitingArea seat status based on rules
    for seating.
    """
    return [
        [
            next_value2(wa, i, j)
            for j, col in enumerate(row)
        ]
        for i, row in enumerate(wa)
    ]

def final_seating2(wa: WaitingArea) -> int:
    """
    Keeps updatiing WaitingArea according to the seat
    rules until no more changes occur. Returns the
    total number of occupied seats.
    """

    # keep updating waiting area until no more changes
    while True:
        next_wa = step2(wa)
        if next_wa == wa: break
        else: wa = next_wa

    # return sum of occupied seats in final waiting area    
    return sum(seat == '#' for row in wa for seat in row)

# unit test

RAW = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL"""

assert final_seating(parse(RAW)) == 37
assert final_seating2(parse(RAW)) == 26

# do the thing

with open('./data/day11.txt') as f:
    raw = f.read()

print('Part 1:', final_seating(parse(raw)))
print('Part 2:', final_seating2(parse(raw)))

