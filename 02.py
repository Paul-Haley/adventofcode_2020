if __name__ == '__main__':
    good = 0
    for line in open("input02.txt").readlines():
        rule, letter, pw = line.strip().split()
        min, max = rule.split('-')
        letter = letter[0]
        occurrence = 0
        for c in pw:
            if c == letter:
                occurrence += 1
        if int(min) <= occurrence <= int(max):
            good += 1
    print(good)
