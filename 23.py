from sys import argv

MOVES = 10000000
MAX_CUPS = 1000000


def to_cups(cup_str):
    cups = dict()
    for ci in range(len(cup_str)):
        cnext = int(cup_str[ci + 1]) if ci < len(cup_str) - 1 else len(cup_str) + 1
        cups[int(cup_str[ci])] = int(cnext)
    for i in range(len(cup_str) + 1, MAX_CUPS + 1):
        cups[i] = i + 1
    cups[MAX_CUPS] = int(cup_str[0])

    return cups


if __name__ == '__main__':
    cup_input = argv[1]
    cups = to_cups(cup_input)
    max_cup = sorted(cups.keys())[-1]
    current = int(cup_input[0])
    for _ in range(MOVES):
        end_cup = cups[cups[cups[current]]]
        dest = current - 1
        while dest < 1 or dest > max_cup or dest in (cups[current], cups[cups[current]], end_cup):
            if dest < 1:
                dest = max_cup
            else:
                dest -= 1

        old_current_next = cups[current]
        cups[current] = cups[end_cup]
        cups[end_cup] = cups[dest]
        cups[dest] = old_current_next

        current = cups[current]
    print(cups[1] * cups[cups[1]])
