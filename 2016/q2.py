"""
2016 Q2: Migration

This is basically just Conway's Game of Life [0], with an extra rule.

https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life
"""

from collections import defaultdict


def coordinate_of_sequence(sequence):
    """
    ___0__1__2__3__4__
    4| 1  2  3  4  5
    3| 6  7  8  9  10
    2| 11 12 13 14 15
    1| 16 17 18 19 20
    0| 21 22 23 24 25
    """

    y = 4 - ((sequence - 1) // 5)
    x = (sequence - 1) % 5

    return x, y


def solve(position, sequence_values, steps):
    state = defaultdict(int)
    sequence_index = 0

    for _ in range(steps):
        new_state = state.copy()

        x, y = coordinate_of_sequence(position)

        # add a new person to the landscape
        new_count = state[x, y] + 1
        new_state[x, y] = new_count

        worklist = [(x, y)]

        while len(worklist) > 0:
            x, y = worklist.pop()

            if new_state[x, y] == 4:
                new_state[x, y] -= 4
                # spread out
                for dx in (-1, 1):
                    new_state[x + dx, y] += 1
                    worklist.append((x + dx, y))
                for dy in (-1, 1):
                    new_state[x, y + dy] += 1
                    worklist.append((x, y + dy))

        position += sequence_values[sequence_index]

        if position > 25:
            position -= 25

        sequence_index = (sequence_index + 1) % len(sequence_values)
        state = new_state

    return state


def print_solution(solution):
    lines = []
    for y in range(5):
        y = 4 - y
        lines.append(
            " ".join(str(solution[x, y] if (x, y) in solution else 0) for x in range(5))
        )

    print("\n".join(lines))


if __name__ == "__main__":
    position, sequence_size, steps = tuple(int(x) for x in input().split())

    sequence_values = [int(input()) for _ in range(sequence_size)]

    solution = solve(position, sequence_values, steps)

    print_solution(solution)
