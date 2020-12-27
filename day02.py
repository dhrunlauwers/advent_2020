from collections import Counter
from typing import List

def parse(inputs: List[int]) -> int:
    """
    checks how many passwords are correct based on rules provided:
    
    breaks each string in inputs down into its components:
    passw - the password string
    char - the character to check
    hi - the highest number of times char should appear in passw
    lo - the lowest number of times char should appear in passw

    counts the number of times the password rules are met
    """

    correct = 0

    for pw in inputs:
        hilo, char, passw = pw.split()
        lo, hi = hilo.split('-')
        counts = Counter(passw)[char[0]]
    
        if int(lo) <= counts <= int(hi): correct = correct + 1

    return correct

def parse2(inputs: List[int]) -> int:
    """
    checks how many passwords are correct based on rules provided:
    
    breaks each string in inputs down into its components:
    passw - the password string
    char - the character to check
    pos1 - the position where char should appear in passw
    pos2 - the second position where char should appear in passw

    counts the number of times the password rules are met
    """

    correct = 0

    for pw in inputs:
        hilo, char, passw = pw.split()
        pos1, pos2 = hilo.split('-')

        check1 = passw[int(pos1)-1] == char[0]
        check2 = passw[int(pos2)-1] == char[0]

        if check1 != check2: correct = correct + 1

    return correct

PASSWORDS = [
    "1-3 a: abcde",
     "1-3 b: cdefg",
    "2-9 c: ccccccccc"
]

assert parse(PASSWORDS) == 2
assert parse2(PASSWORDS) == 1

with open('./data/day02.txt') as f:
    inputs = [line.strip() for line in f]
    print("Part 1: ", parse(inputs))
    print("Part 2: ", parse2(inputs))