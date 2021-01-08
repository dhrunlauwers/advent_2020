# import stuff
import re

# define some functions
def initialize(instructions):
    # initialize memory
    memory = {}

    # split instructions into different programs
    programs = instructions.split('\nmask = ')

    # run each program and update memory
    for program in programs:
        run(program, memory)

    # sum all remaining memory values as checksum
    total = 0
    for line in memory.values():
        total += int(line, 2)

    return total

def run(routine, memory):
    # split routine into mask and program
    lines = routine.split('\n')
    mask = lines[0].replace("mask = ","")
    program = []

    # for each line in the program, decode the instructions into binary
    # and initialize memory
    for line in lines[1:]:
        mem, val = line.split(' = ')
        mem = re.findall(r"[0-9]+", mem)[0]
        memory[mem] = None
        program.append({mem:"{0:036b}".format(int(val))})

    return run_program(mask, memory, program)

def apply_mask(value, mask):
    # applies mask to instructions

    new_value = list(value)
    
    for i, val in enumerate(mask):
        if val != 'X':
            new_value[i] = val
    
    return "".join(new_value)

def run_program(mask, memory, program):

    # runs the given program by updating memory based on
    # instructions after applying the mask
    for line in program:
        for k, v in line.items():
            memory[k] = apply_mask(v, mask)
    
    return memory
    

# unit test
RAW = """mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0"""

assert initialize(RAW) == 165

# do the thing

with open("./data/day14.txt") as f:
    raw = f.read()

print("Part 1:", initialize(raw))