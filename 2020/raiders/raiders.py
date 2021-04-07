"""
0 4 2 1 3 5

start with 1 (though arbitrary of 1,2,3,4 would be fine)

1 <--> 0 --> 1 4 2 0 3 5

then the thing in position 1

4 <--> 5 --> 1 5 2 0 3 4

then the thing in position 4

3 <--> 4 --> 1 5 2 0 4 3

then the thing in position 3

0 <--> 3 --> 1 5 2 3 4 0

Then the thing in position 0 (so put it in its rightful place?)

5 <--> 1 --> 5 1 2 3 4 0

then the thing in position 5

0 <--> 5 --> 0 1 2 3 4 5
"""


def solve(problem):
    solution = []
    correct = list(range(len(problem)))

    first_idol_num, first_idol_pos = min(
        (x, i) for (i, x) in enumerate(problem) if i != x
    )

    problem[first_idol_pos] = problem[0]
    problem[0] = first_idol_num

    last_moved = first_idol_num

    moves = set()
    moves.add((0, first_idol_pos))
    solution.append((0, first_idol_num))

    while correct != problem:
        # print(starting, last_moved)
        if problem[last_moved] == last_moved:
            last_moved, _ = min((i, x) for (i, x) in enumerate(problem) if i != x)

        if last_moved == 0:
            # try putting the thing in position 0 in the right place
            last_moved = problem[0]

            tmp = problem[last_moved]
            problem[last_moved] = last_moved
            problem[0] = tmp

            solution.append((problem[0], last_moved))
            moves.add((0, last_moved))
            continue

        if (last_moved, len(problem) - 1) in moves:
            print ("BUG (%d, %d)" % (last_moved, len(problem) - 1), moves)
            pass

        tmp = problem[last_moved]
        problem[last_moved] = problem[-1]
        problem[-1] = tmp

        solution.append((problem[last_moved], problem[-1]))

        moves.add((last_moved, len(problem) - 1))

        last_moved = tmp

    return solution 


if __name__ == "__main__":
    num_idols = int(input())

    starting = [0] + [int(input()) for _ in range(num_idols)] + [num_idols + 1]

    for (l, r) in solve(starting):
        print(l, r)
        
    print(-1, -1)
