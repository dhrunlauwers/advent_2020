# import stuff

# define some functions
class Program():
    
    def __init__(self, instructions):
        self.instructions = instructions
        self.accumulator = 0

    def parse_instructions(self):
        self.instructions = [{line.split(' ')[0]:{'op':line.split(' ')[1][0], 'val':int(line.split(' ')[1][1:]), 'executed':False}} for line in self.instructions.split('\n')]

    def edit_instructions(self):
        for line in self.instructions:
            pass


    def execute(self):

        self.accumulator = 0
        run = True
        line = 0

        while run:
            if line == len(self.instructions) + 1: 
                print('ending normal execution')
                return True
            ins = self.instructions[line]
            for k, v in ins.items():

                #print(line, k, v)
                
                if v['executed'] == True: 
                    print('infinite loop.. terminating')
                    return False
                
                self.instructions[line][k]['executed'] = True
                
                if k == 'nop': 
                    line += 1
                
                if k == 'acc':
                    line += 1
                    if v['op'] == '-':
                        self.accumulator -= v['val']
                    else: self.accumulator += v['val']
                
                if k == 'jmp':
                    if v['op'] == '-':
                        line -= v['val']
                    else: line += v['val']

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

p_test = Program(RAW)
p_test.parse_instructions()
p_test.execute()
assert p_test.accumulator == 5

# do the thing

with open('./data/day08.txt') as f:
    raw = f.read()

p = Program(raw)
p.parse_instructions()
p.execute()
print(p.accumulator)

p = Program(raw)
p.parse_instructions()
p.edit_instructions()
p.execute()
print(p.accumulator)
