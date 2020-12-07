empty = '.'
tree = '#'

right = 3
down = 1


def read_map():
    return [line.strip() for line in open("input03.txt")]


def extend_map(m, r, d):
    for i in range(len(m)):
        m[i] = m[i] * (len(m) // d) * r
    return m


if __name__ == '__main__':
    map = extend_map(read_map(), right, down)
    x, y = 0, 0
    trees = 0
    while y < len(map):
        if map[y][x] == tree:
            trees += 1
        x += right
        y += down
    print(trees)


