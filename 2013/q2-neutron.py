from __future__ import print_function

try:
    input = raw_input
except:
    pass

# Neutron 
directions = {
    'N':    (0,  1),
    'NE':   (1,  1),
    'E':    (1,  0),
    'SE':   (1, -1),
    'S':    (0, -1),
    'SW':  (-1, -1),
    'W':   (-1,  0),
    'NW':  (-1,  1)
}

S_START = 4
F_START = 0

class Piece:
    def __init__(self, x, y, colour):
        self.x = x
        self.y = y
        self.colour = colour

class Neutron:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Board:
    def __init__(self, f_order, s_order):
        grid = [[None for _ in range(5)] for _ in range(5)]

        self.neutron = Neutron(2, 2)
        grid[2][2] = self.neutron

        for i in range(5):
            grid[F_START][i] = Piece(i, F_START, 'F')

        for i in range(5):
            grid[S_START][i] = Piece(i, S_START, 'S')

        self.f_order = tuple(f_order)
        self.s_order = tuple(s_order)

    def neutron_can_move_to(self, x, y):
        dx = x - self.neutron.x 
        dy = y - self.neutron.y

        if abs(dx) == abs(dy):
            # we can move diagonally
            return True
        elif dx == 0 or dy == 0:
            return True
        else:
            return False

    def move_neutron(self, x, y):
        if grid[y][x] is not None:
            grid[y][x] = self.neutron
            grid[self.neutron.y][self.neutron.y] = None
            
            self.neutron.x = x
            self.neutron.y = y
        else:
            raise ValueError("Invalid Neutron Location")

    def play_first_move(self):
        # move the neutron first

        # see if there is an instant winning move
        for x in range(5):
            if self.neutron_can_move_to(x, 4):
                # win!
                return True

        # 


    def __repr__(self):
        output = ''
        for y in range(5):
            for x in range(5):
                if self.grid[y][x] is None:
                    output += '.'
                elif isinstance(self.grid[y][x], Neutron):
                    output += '*'
                else:
                    output += self.grid[y][x].colour
            output += '\n'
        return output