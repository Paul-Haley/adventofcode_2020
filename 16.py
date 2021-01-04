

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


def remove_invalid(rules, nearby_tickets):
    for ticket in nearby_tickets:
        for number in ticket:
            for rule in rules:
                if rule[1] <= number <= rule[2] or rule[3] <= number <= rule[4]:
                    break
            else:
                nearby_tickets.remove(ticket)


def identify_possible_columns(rules, nearby_transpose):
    rules_to_columns = dict()
    for ci in range(len(nearby_transpose)):
        for ri in range(len(rules)):
            rule = rules[ri]
            for number in nearby_transpose[ci]:
                if not (rule[1] <= number <= rule[2] or rule[3] <= number <= rule[4]):
                    break
            else:
                rule_columns = rules_to_columns.get(ri, set())
                rule_columns.add(ci)
                rules_to_columns[ri] = rule_columns
    return rules_to_columns


if __name__ == '__main__':
    f = open("input16.txt").read()
    parts = f.split("\n\n")
    rules = get_rules(parts[0])
    your_ticket = read_ticket(parts[1])[0]
    nearby_tickets = read_ticket(parts[2])
    remove_invalid(rules, nearby_tickets)
    nearby_transpose = list(map(list, zip(*nearby_tickets)))
    rules_to_columns = identify_possible_columns(rules, nearby_transpose)
    # for rule in sorted(rules_to_columns):
    #     print(rule, rules_to_columns[rule])
    confirmed_column_mappings = dict()
    while len(confirmed_column_mappings) != len(rules):
        identified_column = -1
        for rule in rules_to_columns:
            if len(rules_to_columns[rule]) == 1:
                column = rules_to_columns[rule].pop()
                confirmed_column_mappings[rule] = column
                identified_column = column
                rules_to_columns.pop(rule)
                break
        if identified_column != -1:
            for rule in rules_to_columns:
                rules_to_columns[rule].discard(identified_column)
    print(confirmed_column_mappings)