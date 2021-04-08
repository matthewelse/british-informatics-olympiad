class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Game:
    """
    Representation of triangular coordinates

      
    """

    def __init__(self, players):
        self.grid = {}
        self.grid[0, 0] = 0
        self.player_positions = {}
        self.player_moves = {}
        self.player_points = {}
        self.top_left_filled = (0, 0)

        for i, num_moves in enumerate(players):
            self.player_positions[i + 1] = (0, 0, "L")
            self.player_moves[i + 1] = num_moves
            self.player_points[i + 1] = 0

    def is_upward_pointing_triangle(self, x, y):
        return x % 2 == y % 2

    def adjacent_position(self, x, y, direction):
        if direction == "L":
            return x - 1, y, "R"
        elif direction == "R":
            return x + 1, y, "L"
        elif direction == "V":
            # move vertically, along the horizontal edge of the triangle
            if self.is_upward_pointing_triangle(x, y):
                return x, y - 1, "V"
            else:
                return x, y + 1, "V"
        else:
            assert False

    def next_edge_clockwise(self, x, y, direction):
        if self.is_upward_pointing_triangle(x, y):
            sequence = {"L": "R", "R": "V", "V": "L"}
        else:
            sequence = {"L": "V", "V": "R", "R": "L"}

        return sequence[direction]

    def traverse_filled_region_once(self, x, y, starting_edge):
        edge = starting_edge

        edge = self.next_edge_clockwise(x, y, edge)
        p_x, p_y, p_edge = self.adjacent_position(x, y, edge)

        while (p_x, p_y) in self.grid:
            #  can't move to this edge, move over and see
            x, y, edge = p_x, p_y, p_edge
            edge = self.next_edge_clockwise(x, y, edge)
            p_x, p_y, p_edge = self.adjacent_position(x, y, edge)

        return (x, y, edge)

    def fill(self, x, y, player):
        assert (x, y) not in self.grid

        self.grid[x, y] = player
        self.top_left_filled = (
            min(x, self.top_left_filled[0]),
            min(y, self.top_left_filled[1]),
        )

    def follow_path(self, x, y, path):
        for direction in path:
            x, y, _ = self.adjacent_position(x, y, direction)
        return (x, y)

    def filling_triangle_would_score_points(self, x, y):
        possible_direction_combos = [
            [["R", "R"], ["R", "V"]],
            [["L", "L"], ["L", "V"]],
            [["V", "L"], ["V", "R"]],
        ]

        for required_combos in possible_direction_combos:
            both = True
            for combo in required_combos:
                fx, fy = self.follow_path(x, y, combo)
                if (fx, fy) not in self.grid:
                    both = False
                    break

            if both:
                return True

        return False

    def loop_and_fill(self, player):
        moves = self.player_moves[player]
        start_x, start_y, start_edge = self.player_positions[player]
        x, y, edge = start_x, start_y, start_edge

        for _ in range(moves):
            x, y, edge = self.traverse_filled_region_once(x, y, edge)

            fx, fy, _ = self.adjacent_position(x, y, edge)

            if self.filling_triangle_would_score_points(fx, fy):
                # print('stopping early because of (%d,%d)' % (fx, fy))
                break

        fill_x, fill_y, _ = self.adjacent_position(start_x, start_y, start_edge)

        if self.filling_triangle_would_score_points(fill_x, fill_y):
            self.player_points[player] += 1

        self.fill(fill_x, fill_y, player)

        self.player_positions[player] = x, y, edge

        top_x, top_y = self.top_left_filled

        for player, (x, y, edge) in self.player_positions.items():
            adj_x, adj_y, _ = self.adjacent_position(x, y, edge)

            if (adj_x, adj_y) in self.grid:
                # move to top-left
                # print('hoisting player %d to (%d, %d)' % (player, top_x, top_y))
                self.player_positions[player] = top_x, top_y, "L"

    def perimiter_length(self):
        start_x, start_y = self.top_left_filled
        x, y = start_x, start_y
        edge = "L"
        total = 1

        while True:
            x, y, edge = self.traverse_filled_region_once(x, y, edge)

            if x == start_x and y == start_y and edge == "L":
                break

            total += 1

        return total


if __name__ == "__main__":
    num_players, moves = tuple(int(x) for x in input().split())

    players = [int(x) for x in input().split()]

    game = Game(players)

    for m in range(moves):
        player = (m % num_players) + 1
        game.loop_and_fill(player)

    for i in range(num_players):
        player = i + 1
        print(game.player_points[player])

    print(game.perimiter_length())

