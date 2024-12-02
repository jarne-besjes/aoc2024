

def get_data():
    with open("aoc/input/day2.txt") as f:
        lines = f.readlines()
        return lines

def part1(data):
    total = 0

    points_list = []
    for line in data:
        points_list.append(list(map(int, line.split())))

    for points in points_list:
        success = check_values(points)[0]
        if success:
            total += 1

    print("Day2 part 1:", total)

def check_values(points):
    incr: bool | None = None
    for i in range(len(points) - 1):
        diff = points[i+1] - points[i]

        if incr is None:
            incr = diff > 0

        if not incr:
            diff = - diff

        if 1 <= diff <= 3:
            continue
        else:
            return False, i + 1

    return True, None


def part2(data):
    total = 0

    points_list = []
    for line in data:
        points_list.append(list(map(int, line.split())))

    for points in points_list:
        ret = check_values(points)
        if ret[0]:
            total += 1
            continue
        else:
            for i in range(len(points)):
                # Create a new list excluding the i-th element
                modified_points = points[:i] + points[i + 1:]
                if check_values(modified_points)[0]:
                    total += 1
                    break


    print("Day2 part 2:", total)



def run():
    data = get_data()

    part1(data)
    part2(data)