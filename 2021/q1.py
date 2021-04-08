def  is_pat(s):
    """
    all letters in left string are later then all the letters in the right string, and left and right are both pats
    """

    if len(s) == 1:
        return True
    
    for split_point in range(1, len(s)):
        l, r = s[:split_point], s[split_point:]

        if min(*l) > max(*r):
            if is_pat(list(reversed(l))) and is_pat(list(reversed(r))):
                return True

    return False

if __name__ == '__main__':
    s1, s2 = input().split()

    for s in [s1, s2, s1 + s2]:
        print("YES" if is_pat(s) else "NO")