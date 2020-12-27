def parse(slope):
    """
    Checks all x,y coordinates in a slope and collects 
    all coordinates that contains a tree (#)
    """

    trees = set()
    
    for y, row in enumerate(slope.split('\n')):

        for x, val in enumerate(row):

            if val == "#":
                trees.add((x,y))
    
    return trees

def traverse(slope, right, down):
    """
    Moves down a given slope with a given trajectory
    (right, down) and returns the number of trees encountered
    along the way (hits)
    """

    trees = parse(slope)
    height = len(slope.split('\n'))
    width = len(slope.split('\n')[0])
    hits = 0

    for step in range(int(height / down)):
        loc = (step*right % width, step*down)

        if loc in trees:
            hits = hits + 1

    return hits


SLOPE = """..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#"""

RIGHT = 3
DOWN = 1

TRAJECTORIES = [
    (1,1),
    (3,1),
    (5,1),
    (7,1),
    (1,2)
]

assert traverse(SLOPE, RIGHT, DOWN) == 7

with open('./data/day03.txt') as f:
    inputs = f.read()
    print("Part 1:", traverse(inputs, RIGHT, DOWN))

    total = 1
    for right, down in TRAJECTORIES:
        total = total * traverse(inputs, right, down)
    
    print("Part 2:", total)



