# construct a graph of a particular number
from collections import defaultdict

l = input()
w = input()

source = tuple(int(x) for x in w)
seen = set()

def analyse(number, connections=defaultdict(set)):
    if number in seen:
        return connections

    seen.add(number)

    # look for valid transformations
    for ix in range(len(number) - 1):
        i = number[ix]
        j = number[ix + 1]

        ll, rl = i, i

        if ix >= 1:
            ll = number[ix - 1]
        if ix < len(number) - 2:
            rl = number[ix + 2]

        small, large = min(i, j), max(i, j)

        if (small < ll and large > ll) or (small < rl and large > rl):
            # can swap i and j
            lnumber = list(number)
            lnumber[ix], lnumber[ix + 1] = j, i

            pair = tuple(lnumber)

            connections[number].add(pair)
            connections[pair].add(number)

    for c in connections[number]:
        analyse(c, connections)

    return connections

connections = analyse(source)

def bfs_depth_from_root(root):
    look = [(root, 0)]
    depths = {root: 0}
    seen = set()

    while len(look) > 0:
        step, depth = look.pop(0)
        seen.add(step)

        depths[step] = depth

        for c in connections[step]:
            if c in seen:
                continue

            look.append((c, depth + 1))

    return depths

depths = bfs_depth_from_root(source)
print(max(depths.values()))

