#!/usr/bin/env python3

def step(x):
    out = []

    for i in range(len(x) - 1):
        if x[i] == x[i+1]:
            out.append(x[i])
        else:
            if x[i] != 'R' and x[i+1] != 'R':
                out.append('R')
            elif x[i] != 'G' and x[i+1] != 'G':
                out.append('G')
            elif x[i] != 'B' and x[i+1] != 'B':
                out.append('B')

    return ''.join(out)

if __name__ == '__main__':
    example = input()

    for _ in range(len(example) - 1):
        example = step(example)

    print(example)
