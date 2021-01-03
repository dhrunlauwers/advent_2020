# import stuff

# define some functions
def sum_of_all_nums(nums):
    """
    Returns the sum of all pairs of numbers in the list provided as input.
    """

    return set([x + y for x in nums for y in nums if x != y])

def sum_of_all_cont_nums(nums, set_len):
    """
    Returns set of the sum of all contigious sets of length set_len
    found in nums 
    """

    return {sum(nums[i:i+set_len]):nums[i:i+set_len] for i in range(len(nums) - set_len - 1)}

def parse(xmas_cypher):
    """
    Splits string cypher into list of integers for decryption.
    """

    return [int(x) for x in xmas_cypher.split('\n')]

def decrypt(xmas_cypher, preamble_length):
    """
    Checks provided cypher to see which numbers meet criteria
    for XMAS cypher. Returns the number that did not meet
    criteria: each number after the preamble should be the sum
    of a pair of numbers in the preamble.
    """

    cypher = parse(xmas_cypher)

    for i, x in enumerate(cypher[preamble_length:]):

        preamble = cypher[i:i+preamble_length]

        if x not in sum_of_all_nums(preamble): return x

def find_weakness(xmas_cypher, key):
    """
    Searches for contigious set of numbers that adds up to key found
    during decryption process. Returns the num of the highest and 
    lowest value in the set.
    """
    
    cypher = parse(xmas_cypher)

    possible_set_lengths = range(2,len(cypher))

    for set_len in possible_set_lengths:

        nums_to_check = sum_of_all_cont_nums(cypher, set_len)
        
        if key in nums_to_check: 
            return min(nums_to_check[key]) + max(nums_to_check[key])

# unit test

preamble_len = 5

RAW = """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576"""

assert decrypt(RAW, preamble_len) == 127
assert find_weakness(RAW, decrypt(RAW, preamble_len)) == 62

# do the thing

with open('./data/day09.txt') as f:
    raw = f.read()

print("Part 1: ", decrypt(raw, 25))
print("Part 2: ", find_weakness(raw, decrypt(raw, 25)))