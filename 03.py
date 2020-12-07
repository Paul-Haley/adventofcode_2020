from functools import reduce

empty = '.'
tree = '#'

plans = [(1,1),(3,1),(5,1),(7,1),(1,2)]


def read_map():
    return [line.strip() for line in open("input03.txt")]


def extend_map(m, f):
    for i in range(len(m)):
        m[i] = m[i] * f
    return m


if __name__ == '__main__':
    m = read_map()
    f = max([(len(m) // plan[1]) * plan[0] for plan in plans])
    m = extend_map(m, f)
    trees = []
    for plan in plans:
        x, y = 0, 0
        hits = 0
        while y < len(m):
            if m[y][x] == tree:
                hits += 1
            x += plan[0]
            y += plan[1]
        trees.append(hits)
    print(reduce(lambda x, y: x * y, trees))

