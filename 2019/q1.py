"""
BIO 2019 Q1: Palindromes

This ended up being surprisingly difficult, for whatever reason I found it surprisingly difficult
to reason about.

I found it easier to think about how, given a palindrome, I would calculate the following
palindrome. There are ~2 cases:

Odd number of digits: [left][middle][right = reversed(right)]
Even number of digits: [left][right = reversed(right)]

In the first case, we can (hopefully) obviously generate the next palindrome by adding one to the
middle digit, and carrying the one into the left hand side as if you were doing regular addition,
and then reflecting the new value to produce a new palindrome.

In the second case, we can basically do the same thing, but without the middle digit.

And then if we are still 'carrying' anything by the time we get to the end, this becomes a new
left-most digit, and the right most digit becomes the new middle digit.
"""


class Palindrome:
    def __init__(self, left, middle):
        assert middle is None or middle < 10 and middle >= 0

        self.left = list(int(x) for x in str(left))
        self.middle = middle

    def add_one_left(self, carry):
        for i in range(len(self.left)):
            ix = -(i + 1)

            if self.left[ix] == 9:
                self.left[ix] = 0
                carry = True
            else:
                self.left[ix] += 1
                carry = False
                break

        if carry and self.middle is None:
            self.middle = self.left[-1]
            self.left = [1] + self.left[:-1]

        elif carry and self.middle is not None:
            self.left = [1] + self.left
            self.middle = None

    def next_palindrome(self):
        if self.middle is not None:
            if self.middle == 9:
                self.middle = 0
                self.add_one_left(carry=True)
            else:
                self.middle += 1
        else:
            self.add_one_left(carry=False)

    def as_int(self):
        if self.middle is None:
            l = self.left + list(reversed(self.left))
        else:
            l = self.left + [self.middle] + list(reversed(self.left))

        return int("".join(str(x) for x in l))

    @staticmethod
    def of_int(i):
        s = str(i)

        if len(s) % 2 == 0:
            left = [int(x) for x in s[: len(s) // 2]]
            middle = None
        else:
            left = [int(x) for x in s[: len(s) // 2]]
            middle = int(s[len(left)])

        return Palindrome("".join(str(x) for x in left), middle)

    def __str__(self):
        return str(self.as_int())


i = input()
in_int = int(i)

p = Palindrome.of_int(i)

p_int = p.as_int()

if p_int > in_int:
    print(p_int)
else:
    p.next_palindrome()
    print(p)
