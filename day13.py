# import stuff
from functools import reduce
# define some functions

def next_departure(time, bus):

    return time + bus - time % bus

def best_bus(time, dept_times):

    return (min(dept_times) - time) * dept_times[min(dept_times)]

def parse(raw):
    lines = raw.split('\n')
    time = int(lines[0])
    buses = [int(x) for x in lines[1].split(',') if x != 'x']
    dept_times = {next_departure(time, bus):bus for bus in buses}
    return best_bus(time, dept_times)

def parse2(raw):
    lines = raw.split('\n')
    time = int(lines[0])
    buses = [x for x in lines[1].split(',')]
    offsets = [int(bus) - i for i, bus in enumerate(buses) if bus != 'x']
    return chinese_remainder([int(bus) for bus in buses if bus != 'x'], offsets)

# code from https://rosettacode.org/wiki/Chinese_remainder_theorem#Python_3.6
def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod
 
def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1


# unit test
RAW ="""939
7,13,x,x,59,x,31,19"""

parse(RAW) == 295
parse2(RAW) == 1068781


# do the thing

with open('./data/day13.txt') as f:
    raw = f.read()

print('Part 1:', parse(raw))
print('Part 2:', parse2(raw))