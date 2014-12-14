# A solution to the British Informatics Olympiad 2011 Question 2
# Scores 24/24
from __future__ import print_function

while True:
    try:
        input = raw_input
    except:
        pass

    from collections import deque

    suits = ['C', 'H', 'S', 'D']
    values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']

    def make_deck(suits, values):
        for s in suits:
            for v in values:
                yield (s, v)

    def nice_card(card):
        s, v = card
        return (v + s)

    def shuffle(deck, shuffle_numbers):
        assert len(shuffle_numbers) == 6

        current_number = 0

        while len(deck) != 0:
            for j in range(1, shuffle_numbers[current_number]):
                deck.append(deck.popleft())

            yield deck.popleft()

            current_number += 1
            current_number %= 6

    def make_row(shuffled_deck):
        for i in shuffled_deck:
           yield [i]

    def can_sit_on(a, b):
        return a[0][0] == b[0][0] or a[0][1] == b[0][1]

    def legal_moves(row):
        n = 0
        for i in range(len(row) - 1, -1, -1):
            # see if there are any valid moves
            if i < 1:
                # can't move
                continue

            if can_sit_on(row[i], row[i-1]):
                n += 1

            if i < 3:
                continue

            if can_sit_on(row[i], row[i-3]):
                n += 1

        return n

    def score(row, fr, to):
        row[to] = row.pop(fr) + row[to]
        return legal_moves(row)

    def strategy_1(row):
        status = True
        while status:
            status = _strategy_1(row)

        print(len(row), nice_card(row[0][0]))

    def _strategy_1(row):
        for i in range(len(row) - 1, -1, -1):
            # see if there are any valid moves
            if i < 1:
                # can't move
                continue

            if can_sit_on(row[i], row[i-1]):
                row[i-1] = row.pop(i) + row[i-1]
                return True

            if i < 3:
                continue

            if can_sit_on(row[i], row[i-3]):
                row[i-3] = row.pop(i) + row[i-3]
                return True

        return False

    def strategy_2(row):
        status = True
        while status:
            status = _strategy_2(row)

        print(len(row), nice_card(row[0][0]))

    def _strategy_2(row):
        max_size = -1
        fr = None
        to = None

        for i in range(len(row) - 1, -1, -1):
            # see if there are any valid moves
            if i < 1:
                # can't move
                continue

            if can_sit_on(row[i], row[i-1]):
                size = len(row[i]) + len(row[i-1])

                if size > max_size:
                    fr = i
                    to = i - 1
                    max_size = size

            if i < 3:
                continue

            if can_sit_on(row[i], row[i-3]):
                size = len(row[i]) + len(row[i-3])

                if size > max_size:
                    fr = i
                    to = i - 3
                    max_size = size

        if max_size != -1:
            row[to] = row.pop(fr) + row[to]
            return True

        return False

    def strategy_3(row):
        status = True
        while status:
            status = _strategy_3(row)

        print(len(row), nice_card(row[0][0]))

    def _strategy_3(row):
        best_score = -1
        fr = None
        to = None

        for i in range(len(row) - 1, -1, -1):
            # see if there are any valid moves
            if i < 1:
                # can't move
                continue

            if can_sit_on(row[i], row[i-1]):
                s = score(list(row), i, i - 1)

                if s > best_score:
                    fr = i
                    to = i - 1
                    best_score = s

            if i < 3:
                continue

            if can_sit_on(row[i], row[i-3]):
                s = score(list(row), i, i - 3)

                if s > best_score:
                    fr = i
                    to = i - 3
                    best_score = s

        if best_score != -1:
            row[to] = row.pop(fr) + row[to]
            return True

        return False

    shuffle_numbers = tuple(int(x) for x in input().split())
    deck = list(shuffle(deque(make_deck(suits, values)), shuffle_numbers))
    print(nice_card(deck[0]), nice_card(deck[-1]))

    row = list(make_row(deck))

    # play strategy 1
    strategy_1(list(row))
    # play strategy 2
    strategy_2(list(row))
    # play strategy 3
    strategy_3(list(row))
