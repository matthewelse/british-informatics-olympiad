from itertools import combinations_with_replacement, permutations

def construct_map(r, plan):
    all = set(i for i in range(r))
    chosen = set()

    while len(plan) > 0:
        picked = None

        # pick first room alphabetically
        for i in range(r):
            if i not in chosen and i not in plan:
                picked = i
                chosen.add(picked)
                break

        yield picked, plan[0]

        plan = plan[1:]

    unpicked = all - chosen
    x, y = tuple(unpicked)

    yield x, y

expected = {
    (0, 4),
    (1, 5),
    (2, 6),
    (3, 7),
}
count = 0
total = 0

def pprint(l):
    return "".join(chr(x + ord("A")) for x in l)

for ss in (combinations_with_replacement(range(8), 6)):
    for s in permutations(ss):
        verbose = False
        seen = set()
        total += 1

        for i, (x, y) in enumerate(construct_map(8, s)):
            seen.add((min(x, y), max(x, y)))

            if i == 3 and seen != expected:
                break
            elif i == 3:
                count += 1
                print(pprint(s), count)
                break
    
    # break

print(total, count)
