from itertools import combinations


def read_input(file):
    lines = []
    with open(file) as f:
        for l in f:
            _ = map(int, l.split('x'))
            lines.append(list(_))

    return lines


def solve(input):
    lines = read_input(input)
    area_sum = 0
    peri_vol_sum = 0
    for line in lines:
        c = combinations(line, 2)

        areas = list(map(lambda x: x[0] * x[1], c))
        areas_t = list(map(lambda x: 2*x, areas))

        c = combinations(line, 2)
        perimeters = list(map(lambda x: 2*x[0] + 2*x[1], c))
        volume = line[0] * line[1] * line[2]

        peri_vol_sum += min(perimeters) + volume
        area_sum += sum(areas_t) + min(areas)

    return area_sum, peri_vol_sum


print(solve('input.txt'))
