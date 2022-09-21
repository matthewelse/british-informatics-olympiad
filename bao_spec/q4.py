"""
"""

def solve(end_port, paths):
    step = 0
    positions = {1: []}

    while end_port not in positions:
        next_positions = {}

        for path in paths:
            start_pos = path[step % len(path)]

            if start_pos in positions:
                next_pos = path[(step + 1) % len(path)]
                next_positions[next_pos] = positions[start_pos] + [next_pos]

        step += 1
        positions = next_positions
    
    return positions[end_port][:-1]

def main():
    end_port = int(input())
    num_planes = int(input())
    paths = []

    for _ in range(num_planes):
        path = [int(x) for x in input().split(" ")]
        paths.append(path)

    for step in solve(end_port, paths):
        print(step)

if __name__ == "__main__":
    main()
