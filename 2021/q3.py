from collections import deque

def solve(target):
    target = tuple(target)
    choices = deque([(0, tuple())])

    while len(choices) > 0:
        steps, display = choices.popleft()

        if display == target:
            return steps
        
        # add
        if len(display) < len(target):
            if len(display) == 0:
                next_one = 0
            else:
                next_one = max(display) + 1

            choices.append((steps + 1, display + tuple([next_one])))
    
        # swap
        if len(display) >= 2:
            choices.append((steps + 1, display[1:2] + display[:1] + display[2:]))

        # rotate
        if len(display) >= 2:
            choices.append((steps + 1,  display[1:] + display[:1]))
        
if __name__ == '__main__':
    target = list(ord(x) - ord('A') for x in input())

    warehouse = list(reversed(sorted(target)))

    print(solve(target))
