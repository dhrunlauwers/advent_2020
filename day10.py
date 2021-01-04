# import stuff
from collections import Counter

# define some functions
def parse(raw_input):
    """
    Takes string raw_input and splits it to return list of
    adapters and their joltage.
    """
    return [int(x) for x in raw_input.split('\n')]

def count_diffs(adapter_list):
    """
    Counts the differences in joltage between the
    airplane seat (joltage 0) and the device adapter
    (3 joltages higher than the highest adapter).
    """

    # add joltage for airplane seat
    adapter_list.append(0)
    # add joltage for device adapter
    adapter_list.append(max(adapter_list)+3)
    # sort and count the differences
    adapter_list.sort()
    counts = Counter([(str(adapter_list[i+1] - adapter)) for i, adapter in enumerate(adapter_list[:-1])])

    return counts['1'] * counts['3']
        
def count_paths(adapter_list):
    """
    Counts the number of ways adapters in the adapter list can be arranged
    assuming that the maximum range between adapters is three.
    """

    # add joltage for airplane seat
    adapter_list.append(0)
    # add joltage for device adapter
    adapter_list.append(max(adapter_list)+3)

    goal = adapter_list[-1]

    num_ways = [0] * (goal + 1)
    num_ways[0] = 1

    if 1 in adapter_list:
        num_ways[1] = 1
    
    if 1 in adapter_list and 2 in adapter_list:
        num_ways[2] = 2
    elif 2 in adapter_list: num_ways[2] = 1

    for n in range(3, goal + 1):
        if n not in adapter_list:
            continue

        num_ways[n] = num_ways[n-3] + num_ways[n-2] + num_ways[n-1]
    
    return num_ways[goal]


# unit test
mini_RAW = """16
10
15
5
1
11
7
19
6
12
4"""

RAW = """28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3"""

assert count_diffs(parse(mini_RAW)) == 7 * 5
assert count_diffs(parse(RAW)) == 22 * 10
assert count_paths(parse(mini_RAW)) == 8
assert count_paths(parse(RAW)) == 19208

# do the thing

with open('./data/day10.txt') as f:
    raw = f.read()

print('Part 1:', count_diffs(parse(raw)))
print('Part 2:', count_paths(parse(raw)))