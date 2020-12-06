def get_scores(size, tiles):
    def v(i, j):
        nonlocal size
        return not (
            ((i + 1) % size == 0 and j == i + 1)
            or (i % size == 0 and j == i - 1)
            or (j < 0)
            or (j >= len(tiles))
        )

    t = lambda i, adj: list(filter(lambda j: v(i, j), adj))

    red_adj = {i: [] for i in range(len(tiles))}
    gre_adj = {i: [] for i in range(len(tiles))}
    for (i, tiletype) in enumerate(tiles):
        if tiletype == "1":
            red_adj[i] = t(i, [i - size, i + size])
            gre_adj[i] = t(i, [i - 1, i + 1])
        if tiletype == "2":
            red_adj[i] = t(i, [i - 1, i + 1])
            gre_adj[i] = t(i, [i - size, i + size])
        if tiletype == "3":
            red_adj[i] = t(i, [i - size, i - 1])
            gre_adj[i] = t(i, [i + 1, i + size])
        if tiletype == "4":
            red_adj[i] = t(i, [i - size, i + 1])
            gre_adj[i] = t(i, [i - 1, i + size])
        if tiletype == "5":
            red_adj[i] = t(i, [i + 1, i + size])
            gre_adj[i] = t(i, [i - size, i - 1])
        if tiletype == "6":
            red_adj[i] = t(i, [i - 1, i + size])
            gre_adj[i] = t(i, [i - size, i + 1])

    for adj in [red_adj, gre_adj]:
        for root in adj:
            for (i, node) in enumerate(adj[root]):
                if root not in adj[node]:
                    adj[root].pop(i)

    def cycles(adj):
        nonlocal tiles
        state = ["unvisited"] * len(tiles)
        parents = {}
        times = {}
        time = 0
        score = 0

        def DFS(root):
            nonlocal time, score
            if state[root] == "unvisited":
                state[root] = "visited"
                times[root] = time
                time += 1
                for node in adj[root]:
                    if state[node] == "visited":
                        if node != parents[root]:
                            score += times[root] - times[node] + 1
                        continue
                    parents[node] = root
                    DFS(node)
                state[root] = "processed"

        for i in range(len(tiles)):
            DFS(i)

        return score

    return (cycles(red_adj), cycles(gre_adj))


if __name__ == "__main__":
    size = int(input("> "))
    tiles = []
    for _ in range(size):
        row = input("> ").split()
        tiles += row

    scores = get_scores(size, tiles)
    print(scores[0], scores[1])
