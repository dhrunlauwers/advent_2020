# import stuff
import re
import itertools

# define some functions
class Computer():
    
    def __init__(self):
        self.memory = {}
        self.program = []

    def initialize(self,instructions):
        #decodes instructions into program
        subroutines = instructions.split('\nmask = ')

        for sub in subroutines:
            lines = sub.split('\n')
            mask = lines[0].replace("mask = ","")

            for line in lines[1:]:
                mem, val = line.split(' = ')
                mem = re.findall(r"[0-9]+", mem)[0]

                # transform val to binary
                val = "{0:036b}".format(int(val))

                # apply mask to val
                val = self.apply_mask(val, mask)

                self.program.append({mem:val})

    def initialize2(self, instructions):
        #decodes instructions into program
        subroutines = instructions.split('\nmask = ')

        for sub in subroutines:
            lines = sub.split('\n')
            mask = lines[0].replace("mask = ","")

            for line in lines[1:]:
                mem, val = line.split(' = ')
                mem = re.findall(r"[0-9]+", mem)[0]

                # transform val to binary
                bimem = "{0:036b}".format(int(mem))

                # apply mask to val
                decoder = self.apply_mask2(bimem, mask)

                # decode instruction to get new instructions
                new_ins = self.decode(val, bimem, decoder)

                self.program.extend(new_ins)
    
    def apply_mask2(self, value, mask):
        
        new_value = list(value)

        for i, val in enumerate(mask):
            if val == '0': pass
            else: new_value[i] = val
        
        return "".join(new_value)
    
    def decode(self, value, line, decoder):
        result = []

        to_update=[]
        for i, k in enumerate(decoder):
            if k == 'X': to_update.append(i)

        values = list(map(list,itertools.product([0,1], repeat=len(to_update))))

        for row in values:
            new_res = list(decoder)
            for i, ind in enumerate(to_update):
                new_res[ind] =  str(row[i])
            result.append({int(''.join(new_res),2):"{0:036b}".format(int(value))})

        return result

    def run(self):
        # updates memory based on program
        for line in self.program:
            for k, v in line.items():
                self.memory[k] = v
    
    def memory_checksum(self):
        # sum all remaining memory values as checksum
        total = 0
        for line in self.memory.values():
            total += int(line, 2)

        return total

    def apply_mask(self, value, mask):
        # applies mask to instructions

        new_value = list(value)
        
        for i, val in enumerate(mask):
            if val != 'X':
                new_value[i] = val
        
        return "".join(new_value)


    

# unit test
RAW = """mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0"""

C = Computer()
C.initialize(RAW)
C.run()
assert C.memory_checksum() == 165

RAW2 = """mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1"""

C2 = Computer()
C2.initialize2(RAW2)
C2.run()
assert C2.memory_checksum() == 208

# do the thing

with open("./data/day14.txt") as f:
    raw = f.read()

c = Computer()
c.initialize(raw)
c.run()
print("Part 1:", c.memory_checksum())

c2 = Computer()
c2.initialize2(raw)
c2.run()
print("Part 2:", c2.memory_checksum())