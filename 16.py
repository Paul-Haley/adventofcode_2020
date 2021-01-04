

def get_rules(rule_text):
    rules = []
    for line in rule_text.split('\n'):
        halfs = line.split(": ")
        limits = halfs[1].split(" or ")
        l1 = limits[0]
        l2 = limits[1]
        rules.append((halfs[0], int(l1.split('-')[0]), int(l1.split('-')[1]), int(l2.split('-')[0]), int(l2.split('-')[1])))
    return rules


def read_ticket(ticket_text):
    tickets = []
    first = True
    for line in ticket_text.split('\n'):
        if first or not line:  # skip first and final line
            first = False
            continue
        numbers = line.split(',')
        for i in range(len(numbers)):
            numbers[i] = int(numbers[i])
        tickets.append(numbers)
    return tickets


def apply_rules_part1(rules, nearby_tickets):
    scanning_error_rate = 0
    for ticket in nearby_tickets:
        for number in ticket:
            for rule in rules:
                if rule[1] <= number <= rule[2] or rule[3] <= number <= rule[4]:
                    break
            else:
                scanning_error_rate += number
    return scanning_error_rate


if __name__ == '__main__':
    f = open("input16.txt").read()
    parts = f.split("\n\n")
    rules = get_rules(parts[0])
    your_ticket = read_ticket(parts[1])[0]
    nearby_tickets = read_ticket(parts[2])
    print(apply_rules_part1(rules, nearby_tickets))
