def parse_passport(line):
    passport = dict()
    for i in line.split():
        parts = i.split(':')
        passport[parts[0]] = parts[1]
    return passport

def read_passports():
    passports = []
    current = ''
    for line in open("input04.txt"):
        if not line.strip():
            passports.append(parse_passport(current))
            current = ''
        if not current:
            current = line.strip()
        else:
            current += ' ' + line.strip()
    passports.append(parse_passport(current))
    return passports


if __name__ == '__main__':
    passports = read_passports()
    valid = 0
    for p in passports:
        if len(p) == 8 or len(p) == 7 and not p.get('cid', False):
            valid += 1
    print(valid)