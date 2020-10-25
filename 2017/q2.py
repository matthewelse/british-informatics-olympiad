#!/usr/bin/env python3
from collections import OrderedDict

def vec_add(x, y):
    a, b = x
    c, d = y

    return (a+c, b+d)

def vec_sub(x, y):
    a, b = x
    c, d = y

    return (a - c, b - d)

def in_grid(x, w = 6, h = 6):
    a, b = x

    return a >= 0 and a < w and b >= 0 and b < h

class Grid:
    def __init__(self, w, h):
        self.connections = OrderedDict()
        self.grid = [[0 for _ in range(w - 1)] for _ in range(h - 1)]
        self.w = w
        self.h = h
        self.score = [0, 0]

    def connect(self, from_dot, to_dot, player):
        self.connections[from_dot, to_dot] = player

        # update grid
        boxes = list(self.get_boxes_of_connection(from_dot, to_dot))
        extra = False

        for pos, direction in boxes:
            self.grid[pos[1]][pos[0]] |= 1 << direction

            if player == 0:
                self.grid[pos[1]][pos[0]] &= ~(1 << 4)
            else:
                self.grid[pos[1]][pos[0]] |= 1 << 4

            if self.grid[pos[1]][pos[0]] & 0xF == 0xF:
                # completed box
                self.score[player] += 1
                extra = True

        return extra 

    def find_connection(self, position, player):
        p1_seq = [(0, -1), (1, 0), (0, 1), (-1, 0)]
        p2_seq = [(0, -1), (-1, 0), (0, 1), (1, 0)]

        if player == 0:
            seq = p1_seq
        else:
            seq = p2_seq

        for direction in seq:
            to = vec_add(position, direction)
            if (position, to) not in self.connections and (to, position) not in self.connections:
                if in_grid(position) and in_grid(to):
                    return position, to

        return None

    def get_boxes_of_connection(self, from_dot, to_dot):
        box = vec_add(from_dot, to_dot)
        box = (box[0] / 2, box[1] / 2)

        direction = vec_sub(to_dot, from_dot)

        box_1 = vec_sub(box, (direction[1] / 2, direction[0] / 2))
        box_2 = vec_add(box, (direction[1] / 2, direction[0] / 2))
        
        box_1 = tuple(int(x) for x in box_1)
        box_2 = tuple(int(x) for x in box_2)

        if in_grid(box_1, self.w - 1, self.h - 1):
            if from_dot[0] == to_dot[0] and from_dot[0] > box_1[0]:
                box_1_d = 1
            elif from_dot[0] == to_dot[0] and from_dot[0] == box_1[0]:
                box_1_d = 3
            elif from_dot[1] == to_dot[1] and from_dot[1] > box_1[1]:
                box_1_d = 2
            elif from_dot[1] == to_dot[1] and from_dot[1] == box_1[1]:
                box_1_d = 0
            yield box_1, box_1_d

        if in_grid(box_2, self.w - 1, self.h - 1) and box_2 != box_1:
            if from_dot[0] == to_dot[0] and from_dot[0] > box_2[0]:
                box_2_d = 1
            elif from_dot[0] == to_dot[0] and from_dot[0] == box_2[0]:
                box_2_d = 3
            elif from_dot[1] == to_dot[1] and from_dot[1] > box_2[1]:
                box_2_d = 2
            elif from_dot[1] == to_dot[1] and from_dot[1] == box_2[1]:
                box_2_d = 0
            yield box_2, box_2_d

def get_input():
    line = input().split()
    parts = [int(x) for x in line] 

    player1 = (parts[0] - 1, parts[1])
    player2 = (parts[2] - 1, parts[3])
    turns = parts[4]

    return player1, player2, turns

def print_grid(grid):
    for row in grid:
        line = ''
        for cell in row:
            if cell & 0xF != 0xF:
                line += '* '
            else:
                if cell & 0x10:
                    line += 'O '
                else:
                    line += 'X '
        print(line.strip())

def cartesian_position(position):
    pos = divmod(position,  6) 
    return pos[1], pos[0]

if __name__ == '__main__':
    p1, p2, turns = get_input()
    player = 0
    grid = Grid(6, 6)

    for t in range(turns):
        if player == 0:
            position, step = p1 
        else:
            position, step = p2
        
        position += step
        position %= 36

        position_coordinates = cartesian_position(position)
        con = grid.find_connection(position_coordinates, player)

        while con is None:
            position += 1
            position %= 36

            position_coordinates = cartesian_position(position)
            con = grid.find_connection(position_coordinates, player)

        f, t = con
        extra = grid.connect(f, t, player)

        if player == 0:
            p1 = (position, step)
        else:
            p2 = (position, step)

        if not extra:
            player = 1 - player

    print_grid(grid.grid)

    score = tuple(grid.score) 

    print()
    print('%d %d' % score)

