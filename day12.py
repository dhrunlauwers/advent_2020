# import stuff

# define some functions

class Ship():
    """
    To keep track of ship and waypoint locations, 
    and allow ship and waypoint to move according 
    to instructions provided.
    """

    def __init__(self):
        self.direction = 'E'
        self.x = 0
        self.y = 0
        self.wpx = 10
        self.wpy = 1
    
    def move(self, direction, d):
        if direction == 'N':
            self.y += d
        if direction == 'E':
            self.x += d
        if direction == 'S':
            self.y -= d
        if direction == 'W':
            self.x -= d
        if direction == 'F':
            self.move(self.direction, d)
        if direction == 'R' or direction == 'L':
            self.turn(direction, d)

    def turn(self, direction, degrees):

        dir_map = {'N':0, 'E':90, 'S':180, 'W':270}
        inv_dir_map = {v:k for k, v in dir_map.items()}

        if direction == 'R':
            self.direction = inv_dir_map[(dir_map[self.direction] + (degrees % 360)) % 360] 
        if direction == 'L':
            self.direction = inv_dir_map[(dir_map[self.direction] - (degrees % 360)) % 360] 
    
    def dist(self):
        return abs(self.x) + abs(self.y)
    
    def go(self, instructions):
        for line in instructions.split('\n'):
            self.move(line[0], int(line[1:]))

    def move2(self, direction, d):
        if direction == 'N':
            self.wpy += d
        if direction == 'E':
            self.wpx += d
        if direction == 'S':
            self.wpy -= d
        if direction == 'W':
            self.wpx -= d
        if direction == 'F':
            self.x += self.wpx * d
            self.y += self.wpy * d        
        if direction == 'R' or direction == 'L':
            self.turn2(direction, d)
    
    def turn2(self, direction, degrees):
        d = degrees % 360

        if direction == 'R':
            if d == 90:
                self.wpx, self.wpy = self.wpy, -self.wpx     
            if d == 180:
                self.wpx, self.wpy = -self.wpx, -self.wpy
            if d == 270:
                self.wpx, self.wpy = -self.wpy, self.wpx
            if d == 0: pass
        if direction == 'L':
            if d == 90:
                self.wpx, self.wpy = -self.wpy, self.wpx
            if d == 180:
                self.wpx, self.wpy = -self.wpx, -self.wpy
            if d == 270:
                self.wpx, self.wpy = self.wpy, -self.wpx    
            if d == 0: pass

    def go2(self, instructions):
        for line in instructions.split('\n'):
            self.move2(line[0], int(line[1:]))





# unit test

RAW = """F10
N3
F7
R90
F11"""

s_test = Ship()
s_test.go(RAW)
assert s_test.dist() == 25

s_test2 = Ship()
s_test2.go2(RAW)
assert s_test2.dist() == 286

# do the thing

with open('./data/day12.txt') as f:
    raw = f.read()

s = Ship()
s.go(raw)
print('Part 1:', s.dist())

s2 = Ship()
s2.go2(raw)
print('Part 2:', s2.dist())


