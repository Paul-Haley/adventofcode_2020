n = sorted([int(l.strip()) for l in open("input01.txt").readlines()])

c = 2020
a, b = 0, len(n) - 1
while a < b:
    s = n[a] + n[b]
    if s == c:
        print(n[a]*n[b])
        exit()
    if s < c:
        a += 1
    if s > c:
        b -= 1
