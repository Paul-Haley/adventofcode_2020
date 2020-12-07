if __name__ == '__main__':
    good = 0
    for line in open("input02.txt").readlines():
        rule, letter, pw = line.strip().split()
        a, b = rule.split('-')
        letter = letter[0]
        i, j = pw[int(a) - 1] != letter, pw[int(b) - 1] != letter
        if (i or j) and not (i and j):  # xor
            good += 1
    print(good)
