# A solution to the British Informatics Olympiad 2012 Question 2
# Scores 19/23 Marks

class Station(object):
    def __init__(self, name, up, left, right, lazy=True):
        self.name = name
        self.up = up
        self.left = left
        self.right = right

        assert isinstance(lazy, bool), "Lazy must be boolean"
        self.lazy = lazy
        self.downto = self.left

    def enter_left(self):
        if self.lazy:
            self.downto = self.left
        else:
            if self.downto == self.left:
                self.downto = self.right
            else:
                self.downto = self.left
        return self.up

    def enter_right(self):
        if self.lazy:
            self.downto = self.right
        else:
            if self.downto == self.left:
                self.downto = self.right
            else:
                self.downto = self.left
        return self.up
    
    def enter_front(self):
        return self.downto

    def __str__(self):
        return self.name

stations = {
        'A': Station("A", "D", "E", "F"),
        'B': Station("B", "C", "G", "H"),
        'C': Station("C", "B", "I", "J"),
        'D': Station("D", "A", "K", "L"),
        'E': Station("E", "A", "M", "N"),
        'F': Station("F", "A", "N", "O"),
        'G': Station("G", "B", "O", "P"),
        'H': Station("H", "B", "P", "Q"),
        'I': Station("I", "C", "Q", "R"),
        'J': Station("J", "C", "R", "S"),
        'K': Station("K", "D", "S", "T"),
        'L': Station("L", "D", "T", "M"),
        'M': Station("M", "U", "L", "E"),
        'N': Station("N", "U", "E", "F"),
        'O': Station("O", "V", "F", "G"),
        'P': Station("P", "V", "G", "H"),
        'Q': Station("Q", "W", "H", "I"),
        'R': Station("R", "W", "I", "J"),
        'S': Station("S", "X", "J", "K"),
        'T': Station("T", "X", "K", "L"),
        'U': Station("U", "V", "M", "N"),
        'V': Station("V", "U", "O", "P"),
        'W': Station("W", "X", "Q", "R"),
        'X': Station("X", "W", "S", "T")
    }

flipflop = str(raw_input())

for c in flipflop:
    stations[c].lazy = False

del flipflop

direction = str(raw_input())

current = direction[0]
_next = direction[1]

iterations = int(raw_input())

for i in xrange(iterations):
    # Work out where we are entering _next...

    if stations[_next].left == str(current):
        current = _next
        _next = stations[current].enter_left()
    elif stations[_next].right == str(current):
        current = _next
        _next = stations[current].enter_right()
    else:
        current = _next
        _next = stations[current].enter_front()
    print current
    print _next
