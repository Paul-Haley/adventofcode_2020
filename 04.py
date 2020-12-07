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


def validate_hair(rgb):
    if rgb[0] != '#' or len(rgb) != 7:
        return False
    for c in rgb[1:]:
        if c not in 'abcdef1234567890':
            return False
    return True


if __name__ == '__main__':
    passports = read_passports()
    valid = 0
    for p in passports:
        if len(p) == 8 or len(p) == 7 and not p.get('cid', False):
            if 1920 <= int(p['byr']) <= 2002 \
                    and 2010 <= int(p['iyr']) <= 2020 \
                    and 2020 <= int(p['eyr']) <= 2030 \
                    and ((p['hgt'][-2:] == 'cm' and 150 <= int(p['hgt'][0:-2]) <= 193) or
                         (p['hgt'][-2:] == 'in' and 59 <= int(p['hgt'][0:-2]) <= 76)) \
                    and validate_hair(p['hcl']) \
                    and p['ecl'] in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'} \
                    and p['pid'].isdigit() and len(p['pid']) == 9:
                valid += 1
    print(valid)
