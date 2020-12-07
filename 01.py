def find_comp(n, t):
    a, b = 0, len(n) - 1
    while a < b:
        s = n[a] + n[b]
        if s == t:
            return a, b
        if s < t:
            a += 1
        if s > t:
            b -= 1
    return -1, -1


def find3():
    n = sorted([int(l.strip()) for l in open("input01.txt").readlines()])

    t = 2020
    for i in n:
        a, b = find_comp(n, t - i)
        if n[a] + n[b] + i == t:
            print(n[a] * n[b] * i)
            exit()


if __name__ == "__main__":
    find3()
