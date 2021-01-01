# import stuff

# define some functions
def create_bag_map(inputs: str) -> dict:
    """
    Creates a map out of bag loading instructions provided to identify
    components of each colour of bag provided.
    """

    # split instructions into separate lines, and split each line into inner and outer bag(s)
    bag_map = dict(x.strip('.').split(' bags contain ') for x in inputs.split('\n'))

    # iterate over inner and outer bags
    for k, _ in bag_map.items():
        # split inner bags to capture each color separately
        bag_map[k] = bag_map[k].split(',')

        # iterate over each color in the inner bags, to extract number and color name
        for i, v in enumerate(bag_map[k]):
            
            #remove some extra text
            bag_map[k][i] = v.strip().rstrip('s')[:-4]

            # if no bags in inner bag, replace with none
            if bag_map[k][i] == 'no other': bag_map[k] = None

            # if there is an inner bag, capture the number and colour
            else: bag_map[k][i] = {bag_map[k][i][2:]:int(bag_map[k][i][0])} 

    return bag_map

def find_direct_parents(bag_map: dict, child: str, amount: int) -> set:
    """
    Finds which bags directly contain the child bag in at least the amount provided.
    """

    parents = set()

    for bag in bag_map:
        if bag_map[bag] != None:
            for item in bag_map[bag]:
                for k, v in item.items():
                    if k == child and v >= amount: parents.add(bag)

    return parents

def find_all_parents(bag_map: dict, child: str, amount: int) -> set:
    """
    Recursively checks parents to find all bags that could contain the child bag.
    """

    bags_to_check = [child]
    can_contain = set()

    while bags_to_check:
        bag = bags_to_check.pop()
        for parent in find_direct_parents(bag_map, bag, amount):
            if parent not in can_contain:
                can_contain.add(parent)
                bags_to_check.append(parent)
    
    return can_contain

def unpack_bag(bag_map: dict, bag: str) -> int:
    """
    Recursively unpacks a bag to count the number of bags inside.
    """

    bags_to_unpack = [bag]
    total_bags = 0

    while bags_to_unpack:
        bag = bags_to_unpack.pop()
        if bag_map[bag] != None:
            for content in bag_map[bag]:

                for k, v in content.items():
                    total_bags += v
                    for i in range(v):
                        bags_to_unpack.append(k)
    
    return total_bags


# unit test
RAW = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags."""

bag_map = create_bag_map(RAW)
assert len(find_all_parents(bag_map, 'shiny gold', 1)) == 4

RAW2 = """shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags."""

bag_map2 = create_bag_map(RAW2)
assert unpack_bag(bag_map2, 'shiny gold') == 126

# do the thing

with open('data/day07.txt') as f:
    inputs = f.read()

    bag_map = create_bag_map(inputs)

    print('Part 1:', len(find_all_parents(bag_map, 'shiny gold', 1)))
    print('Part 2:', unpack_bag(bag_map, 'shiny gold'))