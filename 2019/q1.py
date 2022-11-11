def next_palindrome(n: str) -> int:
    l, k = len(n), int(n)
    if not l - 1: return k + 1 if k < 9 else 11
    o, m = l % 2, l // 2
    b = m + 1 if o else m
    s1, s2 = n[:b], n[b:]

    if int(s1[m - 1::-1]) <= int(s2): s1 = str(int(s1) + 1)
    return s1 + s1[m - 1::-1]

print(next_palindrome(input()))
