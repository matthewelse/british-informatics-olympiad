"""
Q1: 'String Theory'

Portal (c_x, c_{x+1}) if 26-c_x = c_{x+1}

When we find such a pair, the first element of the pair becomes a portal for surrounding letters.

if c_{x+1} > c_x, the portal leads to the end of the string, otherwise it leads to the start.

When "teleporting", the letters either side of the portal move to either the start or the end
of the string, in the order they were in before.
"""

NO_PORTAL = -1
FRONT = 0
BACK = 1


def find_first_portal(current_string: str):
    """Returns the first portal in the provided string, if one exists."""

    for i in range(len(current_string) - 1):
        left = ord(current_string[i]) - ord("A")
        right = ord(current_string[i + 1]) - ord("A")

        if 25 - right == left:
            target = BACK if left < right else FRONT
            return (i, target)


def teleport(current_string, portal):
    index, target = portal

    this = current_string[index]
    left = "" if index == 0 else current_string[: index - 1]
    left_neighbour = "" if index == 0 else current_string[index - 1]
    right = current_string[index + 2 :]
    right_neighbour = current_string[index + 1]

    if target == BACK:
        return left + this + right + left_neighbour + right_neighbour
    else:
        return left_neighbour + right_neighbour + left + this + right


def main():
    string = input()
    portal = find_first_portal(string)
    seen = {string}

    while portal is not None:
        string = teleport(string, portal)

        if string in seen:
            return "Indefinite"
        seen.add(string)

        portal = find_first_portal(string)

    return string


if __name__ == "__main__":
    print(main())
