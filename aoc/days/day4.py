def get_input():
    with open("aoc/input/day4.txt") as f:
        lines = f.readlines()
    matrix = []
    for line in lines:
        matrix.append(list(line.strip()))

    return matrix


def is_mas(m, index, direction, word_idx=0) -> int:
    w = "MAS"
    if word_idx == len(w):
        return 1

    i, j = index
    if 0 <= i < len(m) and 0 <= j < len(m[0]) and m[i][j] == w[word_idx]:
        if m[i][j] != w[word_idx]:
            return 0
        return is_mas(m, (i + direction[0], j + direction[1]), direction, word_idx + 1)

    return 0


def is_xmas(m, index, direction=None, word_idx=0) -> int:
    w = "XMAS"
    if word_idx == len(w):
        return 1
    if direction is None:
        n = 0
        for direction in [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]:
            n += is_xmas(m, (index[0] + direction[0], index[1] + direction[1]), direction, word_idx + 1)
        return n
    else:
        i, j = index
        if 0 <= i < len(m) and 0 <= j < len(m[0]) and m[i][j] == w[word_idx]:
            if m[i][j] != w[word_idx]:
                return 0
            return is_xmas(m, (i + direction[0], j + direction[1]), direction, word_idx + 1)

    return 0


def part2(m):
    total = 0
    # find all A occurences
    indices = []
    for i, row in enumerate(m):
        for j, c in enumerate(row):
            if c == "A":
                indices.append((i, j))

    for index in indices:
        if (
                (is_mas(m, (index[0] - 1, index[1] - 1), (1, 1)) or
                 is_mas(m, (index[0] + 1, index[1] + 1), (-1, -1))) and
                (is_mas(m, (index[0] + 1, index[1] - 1), (-1, 1)) or
                 is_mas(m, (index[0] - 1, index[1] + 1), (1, -1)))
        ):
            total += 1

    print(total)


def part1(m):
    total = 0
    # find all X occurencees
    indices = []
    for i, row in enumerate(m):
        for j, c in enumerate(row):
            if c == "X":
                indices.append((i, j))

    for index in indices:
        n = is_xmas(m, index)
        total += n

    print(total)


def run():
    m = get_input()

    part1(m)
    part2(m)

    print("hello, world")
