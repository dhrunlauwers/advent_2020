from typing import List

def parse(inputs: List[int]) -> int:
    """
    Checks to find two elements that add up to 2020,
    and the returns their product.
    """

    deltas = {2020 - i for i in inputs}

    for i in inputs:
        if i in deltas:
            return i * (2020-i)

def parse2(inputs: List[int]):
    """
    Checks to find three elements that add up to 2020,
    and the returns their product.
    """

    deltas = {(i, j) for i in inputs for j in inputs if i != j}

    for x in inputs:
        for (i, j) in deltas:
            if i + j + x == 2020:
                return (i*j*x) 

EXPENSES = [
    1721,
    979,
    366,
    299,
    675,
    1456
]

assert parse(EXPENSES) == 514579
assert parse2(EXPENSES) == 241861950

with open("data/day01.txt") as f:
    inputs = [int(line.strip()) for line in f]
    print("Part 1: ", parse(inputs))
    print("Part 2: ", parse2(inputs))
