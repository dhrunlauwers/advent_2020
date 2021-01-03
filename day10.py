# import stuff

# define some functions
def parse(raw_input):
    """
    Takes string raw_input and splits it to return list of
    adapters and their joltage.
    """
    return [int(x) for x in raw_input.split('\n')]

# unit test
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

parse(RAW)

# do the thing

