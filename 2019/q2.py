L = 3
D = 2
R = 1
U = 0


def rotate(v, dir):
    if dir == "F":
        return v
    elif dir == "L":
        return (v + 3) % 4
    elif dir == "R":
        return (v + 1) % 4
    else:
        assert False


class Game:
    def __init__(self, x, y, n):
        self.positions = []
        self.position = (x, y)
        self.v = U
        self.n = n

    def move(self, direction):
        self.positions.append(self.position)
        self.positions = (
            self.positions[1:] if len(self.positions) == self.n + 1 else self.positions
        )
        cant_move = False

        for i in range(4):
            self.v = rotate(self.v, direction)

            x, y = self.position

            if self.v == L:
                new_position = (x - 1, y)
            elif self.v == R:
                new_position = (x + 1, y)
            elif self.v == U:
                new_position = (x, y + 1)
            elif self.v == D:
                new_position = (x, y - 1)
            else:
                assert False

            if new_position in self.positions:
                # can t go here
                cant_move = True
                direction = "R"
                continue
            else:
                self.position = new_position
                cant_move = False
                break

        if cant_move:
            return "STOP"

    def __str__(self):
        v = "URDL"[self.v]
        return "%d (@ %s) %s (dir: %s)" % (self.n, self.position, self.positions, v)


n, instructions, moves = input().split(" ")
n = int(n)
moves = int(moves)

game = Game(0, 0, n)

for i in range(moves):
    move = instructions[i % len(instructions)]

    if game.move(move) == "STOP":
        break

print("%d %d" % (game.position[0], game.position[1]))

