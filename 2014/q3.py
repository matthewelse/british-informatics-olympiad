from math import comb

n = int(input("> "))


def password(n):
    char = lambda i: chr(65 + i) if i <= 25 else str(i - 26)

    lowest_d_digit = 0

    d = 0
    for i in range(12):
        lowest_d_digit = sum([
            comb(36, 11 - i - j)
            for j in range(11 - i) 
            if j + i < 11
        ])
        if n > lowest_d_digit:
            d = 12 - i
            break

    if n <= 36:
        print(char(n - 1))
    else:
        nth_d_digit = n - lowest_d_digit - 1
        acc = 0
        for i in range(36):
            acc += comb(35 - i, d - 1)
            if nth_d_digit < acc:
                print(char(i), end="")
                password(n - acc)
                break


password(n)
