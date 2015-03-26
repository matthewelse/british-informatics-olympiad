from __future__ import print_function

##### UP IS POSITIVE!!!
##### RIGHT IS POSITIVE!!!

try:
    input = raw_input
except:
    pass

def part_b():
    a,c,m,r = (2,3,17,0)
    for i in range(10):
        
        r = (a*r + c) % m
        if i % 2 == 0:
            print(r)

#part_b()

# board is such a misnomer...
class Board:
    def __init__(self, a, c, m, r_init=0):
        self.grid = [[False for _ in range(10)] for _ in range(10)]
        self.a = a
        self.c = c
        self.m = m
        self.r = r_init

    def _set(self, x, y):
        self.grid[y][x] = True

    def _unset(self, x, y):
        self.grid[y][x] = True

    def place_at(self, x, y, length, horizontal=True):
        #I would rather exit gracefully with a wrong answer...
        #assert length >= 1

        h_m = 1 if horizontal else 0
        v_m = 0 if horizontal else 1

        if x + h_m*length > 10 or y + v_m*length > 10:
            return False            

        # check if valid move
        for i in range(length):
            # check around it too!
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    if y + dy < 0 or x + dx < 0 or x + dx >= 10 or y + dy >= 10:
                        continue
                    if self.grid[y + (v_m * i) + dy][x + (h_m * i) + dx]:
                        #print("AGHHH")
                        return False
        
        for i in range(length):
            self._set(x + (h_m * i), y + (v_m * i))

        return True
            

    def workout_algorithm(self, length):
        self.r = (self.a * self.r + self.c) % self.m

        X = self.r % 10
        Y = ((self.r - X) // 10) % 10

        #print(X,Y)
        #if (length == 1):
        #    input()

        self.r = (self.a * self.r + self.c) % self.m

        if not self.place_at(X, Y, length, self.r % 2 == 0):
            # recursion recursion, let's sing about recursion
            return self.workout_algorithm(length)
        else:
            return "%i %i %s" % (X, Y, "H" if self.r % 2 == 0 else "V")

    def __repr__(self):
        output = ''
        for row in reversed(self.grid):
            output += (''.join(['X' if x else '.' for x in row])) + "\n"
        return output

a, c, m = tuple(int(x) for x in input().split())
lengths = (4, 3, 3, 2, 2, 2, 1, 1, 1, 1)
board = Board(a, c, m)

for l in lengths:
    # go through and place them :)
    print(board.workout_algorithm(l))
    #print(board)
