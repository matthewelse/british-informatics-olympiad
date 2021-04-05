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


if __name__ == "__main__":
    num_idols = int(input())

    correct = [i for i in range(num_idols + 2)]
    starting = [0] + [int(input()) for _ in range(num_idols)] + [num_idols + 1]

    first_idol_num, first_idol_pos = min(
        (x, i) for (i, x) in enumerate(starting) if i != x
    )

    # print("swapping %d and %d" % (first_idol_num, 0))
    starting[first_idol_pos] = starting[0]
    starting[0] = first_idol_num

    last_moved = first_idol_num

    moves = set()
    moves.add((0, first_idol_pos))
    # print(starting)
    print("%d %d" % (0, first_idol_num))

    while correct != starting:
        # print(starting, last_moved)
        if starting[last_moved] == last_moved:
            last_moved, _ = min(
                (i, x)
                for (i, x) in enumerate(starting)
                if i != x
            )
        
        if last_moved == 0:
            # try putting the thing in position 0 in the right place
            last_moved = starting[0]

            tmp = starting[last_moved]
            starting[last_moved] = last_moved
            starting[0] = tmp

            print("%d %d" % (starting[0], last_moved))
            moves.add((0, last_moved))
            continue

        if (last_moved, len(starting) - 1) in moves:
            # input()
            # print ("BUG (%d, %d)" % (last_moved, len(starting) - 1), moves)

            pass

        tmp = starting[last_moved]
        starting[last_moved] = starting[-1]
        starting[-1] = tmp

        print("%d %d" % (starting[last_moved], starting[-1]))

        moves.add((last_moved, len(starting) - 1))

        last_moved = tmp

    # print(starting)
    print(-1, -1)
