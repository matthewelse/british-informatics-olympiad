"""
q3 2019 bio

I'm pretty confident that this solution is correct, but it's too slow for the
later examples. I wonder whether it'd be faster in C
"""

l, prefix = input().split(' ')

l = int(l)

# dfs => stack

count = 0
chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[:l]
prefix = [chars.find(c) for c in prefix]

used = 0
all = 0

for i in range(l):
    all |= 1 << i

for i in prefix:
    used |= 1 << i

stack = [ (prefix, used) ]
mask = 0xFFFFFFFF << l

def is_valid(s, c, used):
    # is it valid to add c to s?
    smallest = None

    for ch in s:
        if smallest is None or ch < smallest:
            smallest = ch
        elif ch > smallest and ch < c:
            return False

    if smallest is not None and c > smallest:
        base = 0x000FFFFF

        if (used & (base << (c + 1))) != (all & (base << (c + 1))):
            print("invalid move: %s (adding %d) (smallest: %d)" % (s, c, smallest))
            return False
        #for i in range(1 + c, l):
        #    if (used & (1 << i)) != 1 << i:
        #        return False

    return True

def can_prune(s, used):
    smallest = None

    for ch in s:
        if smallest is None or ch < smallest:
            smallest = ch
        elif ch > smallest:
            # if there are any remaining chars larger than this, we can't do anything
            # at all
            if used & (0xFFFFFFFF << (ch + 1)) == 0 and ch != l - 1:
                print("pruning %s (smallest: %d) (next : %d) (used : %x)" % (s, smallest, ch, used))
                return True

    return False

while len(stack) > 0:
    #print(stack)
    top, used = stack.pop()
    print(top)

    if used == all:
        count += 1
    elif not can_prune(top, used):
        for c in range(l):
            if used & (1 << c) == 0 and is_valid(top, c, used):
                stack.append((top + [c], used | (1 << c)))
    else:
        print("pruned %s" % top)

print(count)

