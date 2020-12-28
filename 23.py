from sys import argv

MOVES = 100


class Cup:
    def __init__(self, label, next):
        self.label = label
        self.next = next


def to_cups(cup_str):
    cups = dict()
    for ci in range(len(cup_str)):
        cnext = int(cup_str[ci + 1] if ci < len(cup_str) - 1 else cup_str[0])
        cups[int(cup_str[ci])] = Cup(int(cup_str[ci]), int(cnext))
    return cups


if __name__ == '__main__':
    cup_input = argv[1]
    cups = to_cups(cup_input)
    max_cup = sorted(cups.keys())[-1]
    cc = int(cup_input[0])
    for _ in range(MOVES):
        current = cups[cc]

        end_move = cups[cups[cups[current.next].next].next]
        dest = cc - 1
        while dest < 1 or dest > max_cup or dest in (current.next, cups[current.next].next, end_move.label):
            if dest < 1:
                dest = max_cup
            else:
                dest -= 1

        old_current_next = current.next
        current.next = end_move.next
        end_move.next = cups[dest].next
        cups[dest].next = old_current_next

        cc = current.next
    cup = cups[cups[1].next]
    labels = ""
    for _ in range(len(cups) - 1):
        labels += str(cup.label)
        cup = cups[cup.next]
    print(labels)
