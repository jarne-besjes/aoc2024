
def get_input():
    with open("aoc/input/day1.txt") as f:
        lines = f.readlines()
        first_column = []
        second_column = []
        for line in lines:
            first_column.append(int(line.split()[0]))
            second_column.append(int(line.split()[1]))

        return first_column, second_column

def part1(first, second):
    first_sorted = sorted(first)
    second_sorted = sorted(second)

    total = 0
    for i in range(len(first_sorted)):
        total += abs(first_sorted[i] - second_sorted[i])

    print("Day1 part 1:", total)


def part2(first, second):
    first_sorted = sorted(first)
    second_sorted = sorted(second)

    total = 0
    for i in range(len(first_sorted)):
        total += first_sorted[i] * second_sorted.count(first_sorted[i])

    print("Day1 part 2:", total)

def run():
    first, second = get_input()

    part1(first, second)

    part2(first, second)
