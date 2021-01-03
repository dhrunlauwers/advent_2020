# import stuff

def parse_instructions(raw_instructions):
    return [{line.split(' ')[0]:{'op':line.split(' ')[1][0], 'val':int(line.split(' ')[1][1:]), 'executed':False}} for line in raw_instructions.split('\n')]

def execute(ins):

    instructions = ins.copy()
    accumulator = 0
    run = True
    line = 0

    while run:

        if line == len(instructions): 
            return accumulator, True

        ins = instructions[line]
        for k, v in ins.items():
            
            if v['executed'] == True: 
                return accumulator, False
            
            instructions[line][k]['executed'] = True
            
            if k == 'nop': 
                line += 1
            
            if k == 'acc':
                line += 1
                if v['op'] == '-':
                    accumulator -= v['val']
                else: accumulator += v['val']
            
            if k == 'jmp':
                if v['op'] == '-':
                    line -= v['val']
                else: line += v['val']

def fix_program(raw_instructions):

    orig_instructions = parse_instructions(raw_instructions)
    
    lines_to_change = []

    for i, line in enumerate(orig_instructions):
        for k, v in line.items():
            if k == 'nop' or k == 'jmp': lines_to_change.append(i)

    new_ins_list = []
    
    for line_id in lines_to_change:

        orig_instructions = parse_instructions(raw_instructions)
                    
        modified_instructions = orig_instructions.copy()

        for k, v in orig_instructions[line_id].items():

            if k == 'nop': modified_instructions[line_id] = {'jmp':v}
            else: modified_instructions[line_id] = {'nop':v}

            new_ins_list.append(modified_instructions)

    for ins in new_ins_list:
        acc, success = execute(ins)
        if success: return acc

# unit test
RAW = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"""

assert 5, False == execute(parse_instructions(RAW))
assert fix_program(RAW) == 8

# do the thing

with open('./data/day08.txt') as f:
    raw = f.read()

print('Part 1:', execute(parse_instructions(raw)))
print('Part 2:', fix_program(raw))
