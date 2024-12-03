import re


def part1(data):
    total = 0

    mul_instructions = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", data)
    for instruction in mul_instructions:
        total += int(instruction[0]) * int(instruction[1])

    print("day3 part 1:", total)


def part2(data):
    total = 0

    mul_instructions = re.findall(r"(mul\((\d{1,3}),(\d{1,3})\))|(do\(\))|(don\'t\(\))", data)
    enabled: bool = True
    for instruction in mul_instructions:
        if instruction[4] != "":
            enabled = False
        if instruction[3] != "":
            enabled = True
        if enabled:
            if instruction[0] != "":
                total += int(instruction[1]) * int(instruction[2])

    print(total)


def run():
    with open("aoc/input/day3.txt", "r") as f:
        data = f.read()

    part1(data)
    part2(data)
