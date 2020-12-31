# import stuff

# define some functions
def parse_forms(forms: str) -> int:
    """
    Consolidates selections from several customs declaration forms
    by counting the number of unique questions answered for each group of forms.
    """
    
    # turn all characters into a sets and count the length
    return len(set(forms.replace('\n','')))

def parse_forms2(forms:str) -> int:
    """
    Consolidates selections from several customs declaration forms
    by counting the number of common questions answered for each group of forms.
    """
    
    #split group of forms into one form per person
    split_forms = forms.split('\n')

    #start with a set of the first person's answers
    result = set(split_forms[0])

    #only keep the intersection of the first and subsequent forms
    for form in split_forms:
        result.intersection_update(form)

    #return length of the resulting set
    return len(result)


def form_sum(inputs: str, func) -> int:
    """
    Parses all customs forms provided as input, and returns the sum of 
    questions answered based on function provided.
    """
    
    forms_list = inputs.split('\n\n')
    nums_list = list(map(func, forms_list))

    return sum(nums_list)
    
# unit tests
RAW = """abc

a
b
c

ab
ac

a
a
a
a

b"""

assert form_sum(RAW, parse_forms) == 11
assert form_sum(RAW, parse_forms2) == 6

# do the thing
with open('./data/day06.txt') as f:
    inputs = f.read()

    print("Part 1:", form_sum(inputs, parse_forms))
    print("Part 2:", form_sum(inputs, parse_forms2))
