"""
Q2: Alpha Complex

Frustratingly this is too slow for two of the larger examples (test 6 and test
8). I think this is mostly just an issue with Python :(.

Still, only lost 6 marks for to slowness. 18/24.

2b: (i) A (ii) AAAA

2c: The first time we visit a room, all of the exits have been used an even
(zero) number of times. Each time we visit the room, we flip one exit from odd
to even. Add up all of the rooms (1 for odd, 0 for even). If the resulting
number is odd, the room number is even. If the resulting number is even, the
room number is odd. (3/4)

2d: There's probably a clever combinatorical way to calculate this, but I'll
brute force it. 8! = 40k, basically nothing.
"""

"""
Stage 1: construct the map.
"""


def construct_map(r, plan):
    all = set(i for i in range(r))
    connections = [set() for _ in range(r)]
    chosen = set()

    while len(plan) > 0:
        # pick first room alphabetically
        picked = None

        for i in range(r):
            if i not in chosen and i not in plan:
                picked = i
                chosen.add(picked)
                break

        # print("connecting %s and %s" % ((chr(ord("A") + picked), chr(ord("A") + plan[0]))))

        connections[picked].add(plan[0])
        connections[plan[0]].add(picked)

        plan = plan[1:]
        # print("plan = %s" % ("".join(chr(ord("A") + x) for x in plan)))

    unpicked = all - chosen
    x, y = tuple(unpicked)

    # print("connecting %s and %s" % ((chr(ord("A") + x), chr(ord("A") + y))))

    connections[x].add(y)
    connections[y].add(x)

    return connections


plan, p, q = input().split(" ")
p = int(p)
q = int(q)
plan = list(plan)
r = len(plan) + 2

# Rename rooms from letters to numbers. (A=0, B=1 etc.)
plan = [ord(c) - ord("A") for c in plan]
connections = construct_map(r, plan)

# Print the rooms connected to A

connections = [list(sorted(y)) for y in connections]

for i in range(r):
    connected_to_a = []
    for y in connections[i]:
        connected_to_a.append(chr(ord("A") + y))

    print("".join(connected_to_a))

start_room = 0  # A

room_counts = [0 for _ in range(r)]
room_counts[start_room] = 1

# all exists are zero
leave_counts = [[0 for _ in range(r)] for _ in range(r)]

current_room = start_room
move_count = 0

after_p = None
after_q = None

while move_count < q:
    visit_count = room_counts[current_room]

    leave_through = None

    if visit_count % 2 == 1:
        # odd
        # leave through the first exit alphabetically
        leave_through = connections[current_room][0]
    else:
        # even
        # find the first exit alphabetically that they have left through an
        # odd number of times

        exits = connections[current_room]

        for i, exit in enumerate(exits):
            if leave_counts[current_room][exit] % 2 == 1:
                if i == len(exits) - 1:
                    leave_through = exit
                    break
                else:
                    # not the last one, leave through the next one, alphabetically
                    leave_through = exits[i + 1]
                    break

    leave_counts[current_room][leave_through] += 1
    room_counts[leave_through] += 1
    current_room = leave_through

    move_count += 1

    if move_count == p:
        after_p = current_room
    if move_count == q:
        after_q = current_room

print("%s%s" % (chr(ord("A") + after_p), chr(ord("A") + after_q)))
